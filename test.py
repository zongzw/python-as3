
import uuid
import json

from collections import namedtuple
from oslo_config import cfg
from oslo_log import log as logging

from octavia.common import exceptions as o_exceptions

from octavia_f5.common import constants
from octavia_f5.restclient import as3restclient
from octavia_f5.restclient.as3classes import ADC, AS3, Application, Monitor
from octavia_f5.restclient.as3objects import application as m_app
from octavia_f5.restclient.as3objects import pool as m_pool
from octavia_f5.restclient.as3objects import pool_member as m_member
from octavia_f5.restclient.as3objects import service as m_service
from octavia_f5.restclient.as3objects import tenant as m_part

from octavia_f5.utils import driver_utils, exceptions, cert_manager, esd_repo
from octavia_f5.utils.decorators import RunHookOnException

CONF = cfg.CONF
LOG = logging.getLogger(__name__)

def json2AS3Obj(jdata, network_id, segmentation_id):

    action = 'deploy'
    # if CONF.f5_agent.dry_run:
    #     action = 'dry-run'
    decl = AS3(
        persist=True,
        action=action,
        _log_level=LOG.logger.level)
    adc = ADC(
        id="urn:uuid:{}".format(uuid.uuid4()),
        label="F5 BigIP Octavia Provider")
    decl.set_adc(adc)

    # if not CONF.f5_agent.migration and CONF.f5_agent.sync_to_group:
    #     # No group syncing if we are in migration mode
    #     decl.set_sync_to_group(CONF.f5_agent.sync_to_group)

    def dictDecoder(mydict):
        return namedtuple('LBObj', mydict.keys())(*mydict.values())

    lb = json.loads(jdata, object_hook=dictDecoder)

    loadbalancer = lb.loadbalancer
    project_id = loadbalancer.project_id

    tenant = adc.get_or_create_tenant(
        m_part.get_name(network_id),
        defaultRouteDomain=segmentation_id,
        label='{}{}'.format(constants.PREFIX_PROJECT, project_id or 'none')
    )


    # Skip load balancer in (pending) deletion
    if loadbalancer.provisioning_status in [constants.PENDING_DELETE, constants.DELETED]:
        return

    # Create generic application
    app = Application(constants.APPLICATION_GENERIC, label=loadbalancer.id)

    # Attach Octavia listeners as AS3 service objects
    for listener in loadbalancer.listeners:
        if not driver_utils.pending_delete(listener):
            try:
                # service_entities = m_service.get_service(listener, self.cert_manager, self._esd_repo)
                service_entities = m_service.get_service(loadbalancer, listener)
                app.add_entities(service_entities)
            except o_exceptions.CertificateRetrievalException as e:
                LOG.error("Could not retrieve certificate, skipping listener '%s': %s", listener.id, e)

    # Attach pools
    for pool in loadbalancer.pools:
        if not driver_utils.pending_delete(pool):
            app.add_entities(m_pool.get_pool(pool))

    # Attach newly created application
    tenant.add_application(m_app.get_name(loadbalancer.id), app)

    return decl.to_json()
    # # Optionally temporarly select BigIP
    # bigip = self.bigip
    # if device:
    #     for b in self._bigips:
    #         if b.hostname == device:
    #             bigip = b

    # # Workaround for Monitor deletion bug, inject no-op Monitor
    # # tracked https://github.com/F5Networks/f5-appsvcs-extension/issues/110
    # while True:
    #     try:
    #         return bigip.post(json=decl.to_json())
    #     except exceptions.MonitorDeletionException as e:
    #         tenant = getattr(decl.declaration, e.tenant)
    #         application = getattr(tenant, e.application, None)
    #         if not application:
    #             # create fake application
    #             application = Application(constants.APPLICATION_GENERIC, label='HM Workaround App')
    #             tenant.add_application(e.application, application)
    #         application.add_entities([(e.monitor, Monitor(monitorType='http'))])


if __name__ == '__main__':
    with open('/Users/zong/GitRepos/zongzw/python-as3/testdata/loadbalancer-full-create-response.json') as fr:
        jdata = fr.read()
        # print(jdata)
        a = json2AS3Obj(jdata, 'a', 'b')
        print(a)