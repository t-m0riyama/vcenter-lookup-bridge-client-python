"""CLI テスト共通フィクスチャ"""

import pytest
from click.testing import CliRunner
from unittest.mock import MagicMock

from vcenter_lookup_bridge_client.cli.main import cli

# テスト用の共通グローバルオプション
BASE_ARGS = ["--host", "http://localhost", "--username", "test", "--password", "test"]


@pytest.fixture
def cli_runner():
    """CliRunner フィクスチャ"""
    return CliRunner()


@pytest.fixture
def mock_api_client():
    """ApiClient のモック"""
    return MagicMock()


# ---- レスポンスファクトリ ----

def make_vm_response(**kwargs):
    m = MagicMock()
    m.name = kwargs.get("name", "test-vm")
    m.instance_uuid = kwargs.get("instance_uuid", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
    m.vcenter = kwargs.get("vcenter", "vcenter01")
    m.datacenter = kwargs.get("datacenter", "DC1")
    m.vm_folder = kwargs.get("vm_folder", "TestFolder")
    m.num_cpu = kwargs.get("num_cpu", 4)
    m.memory_size_mb = kwargs.get("memory_size_mb", 4096)
    m.hostname = kwargs.get("hostname", "test-vm.example.com")
    return m


def make_vm_detail_response(**kwargs):
    m = make_vm_response(**kwargs)
    m.cluster = kwargs.get("cluster", "Cluster01")
    m.esxi_hostname = kwargs.get("esxi_hostname", "esxi01.example.com")
    m.power_state = kwargs.get("power_state", "poweredOn")
    m.ip_address = kwargs.get("ip_address", "192.168.0.1")
    m.guest_full_name = kwargs.get("guest_full_name", "Red Hat Enterprise Linux 8 (64-bit)")
    m.uuid = kwargs.get("uuid", "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy")
    m.hw_version = kwargs.get("hw_version", "vmx-19")
    m.template = kwargs.get("template", False)
    m.vm_path_name = kwargs.get("vm_path_name", "[DS1] test-vm/test-vm.vmx")
    m.model_dump = MagicMock(return_value={
        "name": m.name, "instance_uuid": m.instance_uuid, "vcenter": m.vcenter,
        "power_state": m.power_state
    })
    return m


def make_vm_list_response(results=None, **kwargs):
    m = MagicMock()
    m.success = True
    m.partial_failure = False
    m.timestamp = "2026-04-16T00:00:00Z"
    m.results = results if results is not None else [make_vm_response()]
    m.pagination = None
    m.model_dump = MagicMock(return_value={
        "success": True,
        "results": [{"name": r.name} for r in m.results],
        "timestamp": m.timestamp,
    })
    return m


def make_vm_get_response(result=None, **kwargs):
    m = MagicMock()
    m.success = True
    m.partial_failure = False
    m.timestamp = "2026-04-16T00:00:00Z"
    m.results = result if result is not None else make_vm_detail_response()
    m.model_dump = MagicMock(return_value={
        "success": True,
        "results": {"name": m.results.name},
        "timestamp": m.timestamp,
    })
    return m


def make_host_response(**kwargs):
    m = MagicMock()
    m.name = kwargs.get("name", "esxi01.example.com")
    m.uuid = kwargs.get("uuid", "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa")
    m.vcenter = kwargs.get("vcenter", "vcenter01")
    m.datacenter = kwargs.get("datacenter", "DC1")
    m.status = kwargs.get("status", "green")
    m.esxi_version = kwargs.get("esxi_version", "7.0.3")
    m.num_cpu_cores = kwargs.get("num_cpu_cores", 16)
    m.memory_size_mb = kwargs.get("memory_size_mb", 131072)
    return m


def make_host_detail_response(**kwargs):
    m = make_host_response(**kwargs)
    m.cluster = kwargs.get("cluster", "Cluster01")
    m.ip_address = kwargs.get("ip_address", "10.0.0.1")
    m.power_state = kwargs.get("power_state", "poweredOn")
    m.cpu_model = kwargs.get("cpu_model", "Intel Xeon Gold 6258R")
    m.hardware_vendor = kwargs.get("hardware_vendor", "Dell")
    m.hardware_model = kwargs.get("hardware_model", "PowerEdge R640")
    m.model_dump = MagicMock(return_value={"name": m.name, "status": m.status})
    return m


def make_host_list_response(results=None):
    m = MagicMock()
    m.success = True
    m.results = results if results is not None else [make_host_response()]
    m.model_dump = MagicMock(return_value={"success": True, "results": [{"name": r.name} for r in m.results]})
    return m


def make_host_get_response(result=None):
    m = MagicMock()
    m.success = True
    m.results = result if result is not None else make_host_detail_response()
    m.model_dump = MagicMock(return_value={"success": True, "results": {"name": m.results.name}})
    return m


def make_cluster_response(**kwargs):
    m = MagicMock()
    m.name = kwargs.get("name", "Cluster01")
    m.vcenter = kwargs.get("vcenter", "vcenter01")
    m.datacenter = kwargs.get("datacenter", "DC1")
    m.num_hosts = kwargs.get("num_hosts", 3)
    m.num_cpu_cores = kwargs.get("num_cpu_cores", 48)
    m.memory_size_mb = kwargs.get("memory_size_mb", 393216)
    return m


def make_cluster_list_response(results=None):
    m = MagicMock()
    m.success = True
    m.results = results if results is not None else [make_cluster_response()]
    m.model_dump = MagicMock(return_value={"success": True, "results": [{"name": r.name} for r in m.results]})
    return m


def make_datastore_response(**kwargs):
    m = MagicMock()
    m.name = kwargs.get("name", "datastore01")
    m.vcenter = kwargs.get("vcenter", "vcenter01")
    m.datacenter = kwargs.get("datacenter", "DC1")
    m.type = kwargs.get("type", "VMFS")
    m.capacity_gb = kwargs.get("capacity_gb", 1024)
    m.free_space_gb = kwargs.get("free_space_gb", 512)
    return m


def make_datastore_list_response(results=None):
    m = MagicMock()
    m.success = True
    m.results = results if results is not None else [make_datastore_response()]
    m.model_dump = MagicMock(return_value={"success": True, "results": [{"name": r.name} for r in m.results]})
    return m


def make_portgroup_response(**kwargs):
    m = MagicMock()
    m.name = kwargs.get("name", "portgroup01")
    m.vcenter = kwargs.get("vcenter", "vcenter01")
    m.datacenter = kwargs.get("datacenter", "DC1")
    m.vlan_id = kwargs.get("vlan_id", 100)
    m.vswitch_name = kwargs.get("vswitch_name", "vSwitch0")
    return m


def make_portgroup_list_response(results=None):
    m = MagicMock()
    m.success = True
    m.results = results if results is not None else [make_portgroup_response()]
    m.model_dump = MagicMock(return_value={"success": True, "results": [{"name": r.name} for r in m.results]})
    return m


def make_vm_folder_response(**kwargs):
    m = MagicMock()
    m.name = kwargs.get("name", "TestFolder")
    m.vcenter = kwargs.get("vcenter", "vcenter01")
    m.datacenter = kwargs.get("datacenter", "DC1")
    m.path = kwargs.get("path", "/DC1/vm/TestFolder")
    return m


def make_vm_folder_list_response(results=None):
    m = MagicMock()
    m.success = True
    m.results = results if results is not None else [make_vm_folder_response()]
    m.model_dump = MagicMock(return_value={"success": True, "results": [{"name": r.name} for r in m.results]})
    return m


def make_snapshot_response(**kwargs):
    m = MagicMock()
    m.name = kwargs.get("name", "snapshot01")
    m.instance_uuid = kwargs.get("instance_uuid", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
    m.vcenter = kwargs.get("vcenter", "vcenter01")
    m.vm_name = kwargs.get("vm_name", "test-vm")
    m.create_time = kwargs.get("create_time", "2026-04-01T00:00:00Z")
    m.description = kwargs.get("description", "Test snapshot")
    return m


def make_snapshot_list_response(results=None):
    m = MagicMock()
    m.success = True
    m.results = results if results is not None else [make_snapshot_response()]
    m.model_dump = MagicMock(return_value={"success": True, "results": [{"name": r.name} for r in m.results]})
    return m


def make_event_response(**kwargs):
    m = MagicMock()
    m.created_time = kwargs.get("created_time", "2026-04-16T00:00:00Z")
    m.event_type = kwargs.get("event_type", "VmPoweredOnEvent")
    m.vcenter = kwargs.get("vcenter", "vcenter01")
    m.event_source = kwargs.get("event_source", "vm01")
    m.user_name = kwargs.get("user_name", "admin")
    m.ip_address = kwargs.get("ip_address", "10.0.0.1")
    m.description = kwargs.get("description", "VM powered on")
    return m


def make_event_list_response(results=None):
    m = MagicMock()
    m.success = True
    m.results = results if results is not None else [make_event_response()]
    m.model_dump = MagicMock(return_value={"success": True, "results": [{"event_type": r.event_type} for r in m.results]})
    return m


def make_alarm_response(**kwargs):
    m = MagicMock()
    m.name = kwargs.get("name", "alarm01")
    m.vcenter = kwargs.get("vcenter", "vcenter01")
    m.datacenter = kwargs.get("datacenter", "DC1")
    m.status = kwargs.get("status", "red")
    m.alarm_source = kwargs.get("alarm_source", "host01")
    m.acknowledged = kwargs.get("acknowledged", False)
    m.created_time = kwargs.get("created_time", "2026-04-16T00:00:00Z")
    m.description = kwargs.get("description", "Test alarm")
    return m


def make_alarm_list_response(results=None):
    m = MagicMock()
    m.success = True
    m.results = results if results is not None else [make_alarm_response()]
    m.model_dump = MagicMock(return_value={"success": True, "results": [{"name": r.name} for r in m.results]})
    return m


def make_vcenter_response(**kwargs):
    m = MagicMock()
    m.name = kwargs.get("name", "vcenter01")
    m.host = kwargs.get("host", "vcenter01.example.com")
    m.version = kwargs.get("version", "7.0.3")
    return m


def make_vcenter_list_response(results=None):
    m = MagicMock()
    m.success = True
    m.results = results if results is not None else [make_vcenter_response()]
    m.model_dump = MagicMock(return_value={"success": True, "results": [{"name": r.name} for r in m.results]})
    return m


def make_admin_response(**kwargs):
    m = MagicMock()
    m.success = kwargs.get("success", True)
    m.message = kwargs.get("message", "Operation completed successfully")
    m.model_dump = MagicMock(return_value={"success": m.success, "message": m.message})
    return m


def make_healthcheck_results(**kwargs):
    m = MagicMock()
    m.status = kwargs.get("status", "ok")
    m.vcenter_service_instances = kwargs.get("vcenter_service_instances", "vcenter01:ok")
    return m


def make_healthcheck_response(result=None):
    m = MagicMock()
    m.success = True
    m.results = result if result is not None else make_healthcheck_results()
    m.model_dump = MagicMock(return_value={"success": True, "results": {"status": m.results.status}})
    return m
