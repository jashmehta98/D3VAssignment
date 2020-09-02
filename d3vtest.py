from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'project ID'  

# The name of the zone for this request.
zone = 'us-east4-c'  

instance_body = {
    "kind": "compute#instance",
    "name": "instance-1",
    "zone": "projects/{project-id}/zones/us-east4-c", 
    "machineType": "projects/{project-id}/zones/us-east4-c/machineTypes/e2-micro",
    "displayDevice": {
        "enableDisplay": "false"
    },
    "metadata": {
        "kind": "compute#metadata",
        "items": []
    },
    "tags": {
        "items": []
    },
    "disks": [
        {
            "kind": "compute#attachedDisk",
            "type": "PERSISTENT",
            "boot": "true",
            "mode": "READ_WRITE",
            "autoDelete": "true",
            "deviceName": "jash2",
            "initializeParams": {
                "sourceImage": "projects/ubuntu-os-cloud/global/images/ubuntu-1804-bionic-v20200821a",
                "diskType": "Disk Type Link",
                "diskSizeGb": " "
            },
            "diskEncryptionKey": {}
        }
        {
            "kind": "compute#attachedDisk",
            "mode": "READ_WRITE",
            "autoDelete": "false",
            "type": "PERSISTENT",
            "deviceName": "disk-1",
            "initializeParams": {
                "diskName": "disk-1",
                "diskType": "Disk type Link",
                "diskSizeGb": "10",
                "description": "D3V Technologies Assignment"
            }
        }
    ],
    "networkInterfaces": [
        {
            "kind": "compute#networkInterface",
            "subnetwork": "link",
            "accessConfigs": [
                {
                    "kind": "compute#accessConfig",
                    "name": "External NAT",
                    "type": "ONE_TO_ONE_NAT",
                    "networkTier": "PREMIUM"
                }
            ],
            "aliasIpRanges": []
        }
    ],
    "metadata": {
        "kind": "compute#metadata",
        "items": [
            {
                "key": "Assignment",
                "value": "D3V Technologies"
            },
            {
                "key": "startup-script",
                "value": "apt-get update -y\n\n# Install Stackdriver logging\ncurl -sSO https://dl.google.com/cloudagents/install-logging-agent.sh\nbash install-logging-agent.sh\n\n# Install Stackdriver monitoring\ncurl -sSO https://dl.google.com/cloudagents/install-monitoring-agent.sh\nbash install-monitoring-agent.sh"
            }
        ]
    },
    "serviceAccounts": [
        {
            "email": "credentials",
            "scopes": [
                "https://www.googleapis.com/auth/cloud-platform"
            ]
        }
    ]
}

request = service.instances().insert(
    project=project, zone=zone, body=instance_body)
response = request.execute()


pprint(response)
