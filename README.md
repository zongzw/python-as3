# python-as3

Given the json-format loadbalancer object, this project will help to convert to the corresponding AS3 declaration.

Refer to the json-format loadbalancer object: `./testdata/loadbalancer-full-create-response.json`, AS3 declaration will be:

```
{
    "action": "deploy",
    "class": "AS3",
    "declaration": {
        "class": "ADC",
        "id": "urn:uuid:d1535c33-3f7c-4db4-8f5a-e29623ae0847",
        "label": "F5 BigIP Octavia Provider",
        "net_a": {
            "class": "Tenant",
            "defaultRouteDomain": "b",
            "label": "project_e3cd678b11784734bc366148aa37580e",
            "lb_607226db-27ef-4d41-ae89-f2a800e9c2db": {
                "class": "Application",
                "hm_7d19ad6c-d549-453e-a5cd-05382c6be96a": {
                    "class": "Monitor",
                    "interval": 3,
                    "label": "a8a2aa3f-d099-4752-8265-e6472f8147f9",
                    "monitorType": "http",
                    "receive": "HTTP/1.0 (200|201|202)",
                    "send": "GET /index.html HTTP/1.0\\r\\nHost: test2.example.com\\r\\n\\r\\n",
                    "targetAddress": "192.0.2.16",
                    "targetPort": 80,
                    "timeout": 10
                },
                "hm_a167402b-caa6-41d5-b4d4-bde7f2cbfa5e": {
                    "class": "Monitor",
                    "interval": 3,
                    "label": "a8a2aa3f-d099-4752-8265-e6472f8147f9",
                    "monitorType": "http",
                    "receive": "HTTP/1.0 (200|201|202)",
                    "send": "GET /index.html HTTP/1.0\\r\\nHost: test2.example.com\\r\\n\\r\\n",
                    "targetAddress": "192.0.2.19",
                    "targetPort": 80,
                    "timeout": 10
                },
                "hm_a8a2aa3f-d099-4752-8265-e6472f8147f9": {
                    "class": "Monitor",
                    "interval": 3,
                    "label": "a8a2aa3f-d099-4752-8265-e6472f8147f9",
                    "monitorType": "http",
                    "receive": "HTTP/1.0 (200|201|202)",
                    "send": "GET /index.html HTTP/1.0\\r\\nHost: test2.example.com\\r\\n\\r\\n",
                    "timeout": 10
                },
                "hm_d5bb7712-26b7-4809-8c14-3b407c0cb00d": {
                    "class": "Monitor",
                    "interval": 3,
                    "label": "d5bb7712-26b7-4809-8c14-3b407c0cb00d",
                    "monitorType": "http",
                    "receive": "HTTP/1.(0|1) (200|201|202)",
                    "send": "GET /index.html HTTP/1.0\\r\\nHost: test1.example.com\\r\\n\\r\\n",
                    "timeout": 10
                },
                "hm_f83832d5-1f22-45fa-866a-4abea36e0886": {
                    "class": "Monitor",
                    "interval": 3,
                    "label": "d5bb7712-26b7-4809-8c14-3b407c0cb00d",
                    "monitorType": "http",
                    "receive": "HTTP/1.(0|1) (200|201|202)",
                    "send": "GET /index.html HTTP/1.0\\r\\nHost: test1.example.com\\r\\n\\r\\n",
                    "targetAddress": "192.0.2.52",
                    "targetPort": 80,
                    "timeout": 10
                },
                "label": "607226db-27ef-4d41-ae89-f2a800e9c2db",
                "listener_73c6c564-f215-48e9-91d6-f10bb3454954": {
                    "class": "Service_TCP",
                    "iRules": [],
                    "label": "https_listener",
                    "persistenceMethods": [],
                    "policyEndpoint": [],
                    "pool": "pool_b0577aff-c1f9-40c6-9a3b-7b1d2a669136",
                    "virtualAddresses": [
                        "203.0.113.50/32"
                    ],
                    "virtualPort": 443
                },
                "listener_95de30ec-67f4-437b-b3f3-22c5d9ef9828": {
                    "class": "Service_HTTP",
                    "iRules": [],
                    "label": "redirect_listener",
                    "persistenceMethods": [],
                    "policyEndpoint": [],
                    "virtualAddresses": [
                        "203.0.113.50/32"
                    ],
                    "virtualPort": 8080
                },
                "listener_a99995c6-4f04-4ed3-a37f-ae58f6e7e5e1": {
                    "class": "Service_HTTP",
                    "iRules": [],
                    "label": "http_listener",
                    "persistenceMethods": [],
                    "policyEndpoint": [],
                    "pool": "pool_c8cec227-410a-4a5b-af13-ecf38c2b0abb",
                    "virtualAddresses": [
                        "203.0.113.50/32"
                    ],
                    "virtualPort": 80
                },
                "pool_b0577aff-c1f9-40c6-9a3b-7b1d2a669136": {
                    "class": "Pool",
                    "label": "https_pool",
                    "loadBalancingMode": "round-robin",
                    "members": [
                        {
                            "adminState": "enable",
                            "enable": true,
                            "ratio": 1,
                            "remark": "f83832d5-1f22-45fa-866a-4abea36e0886",
                            "serverAddresses": [
                                "192.0.2.51"
                            ],
                            "servicePort": 80
                        },
                        {
                            "adminState": "enable",
                            "enable": true,
                            "ratio": 1,
                            "remark": "f83832d5-1f22-45fa-866a-4abea36e0886",
                            "serverAddresses": [
                                "192.0.2.52"
                            ],
                            "servicePort": 80
                        }
                    ],
                    "monitors": [
                        {
                            "use": "hm_d5bb7712-26b7-4809-8c14-3b407c0cb00d"
                        },
                        {
                            "use": "hm_f83832d5-1f22-45fa-866a-4abea36e0886"
                        },
                        {
                            "use": "hm_f83832d5-1f22-45fa-866a-4abea36e0886"
                        }
                    ],
                    "remark": "https_pool"
                },
                "pool_c8cec227-410a-4a5b-af13-ecf38c2b0abb": {
                    "class": "Pool",
                    "label": "rr_pool",
                    "loadBalancingMode": "round-robin",
                    "members": [
                        {
                            "adminState": "enable",
                            "enable": true,
                            "ratio": 1,
                            "remark": "7d19ad6c-d549-453e-a5cd-05382c6be96a",
                            "serverAddresses": [
                                "192.0.2.16"
                            ],
                            "servicePort": 80
                        },
                        {
                            "adminState": "disable",
                            "enable": true,
                            "ratio": 1,
                            "remark": "a167402b-caa6-41d5-b4d4-bde7f2cbfa5e",
                            "serverAddresses": [
                                "192.0.2.19"
                            ],
                            "servicePort": 80
                        }
                    ],
                    "monitors": [
                        {
                            "use": "hm_a8a2aa3f-d099-4752-8265-e6472f8147f9"
                        },
                        {
                            "use": "hm_7d19ad6c-d549-453e-a5cd-05382c6be96a"
                        },
                        {
                            "use": "hm_a167402b-caa6-41d5-b4d4-bde7f2cbfa5e"
                        }
                    ],
                    "remark": "rr_pool"
                },
                "template": "generic"
            }
        },
        "schemaVersion": "3.19.0",
        "updateMode": "selective"
    },
    "logLevel": "warning",
    "persist": true,
    "trace": false
}
```
