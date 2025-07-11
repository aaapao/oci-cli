# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.dbmulticloud.src.oci_cli_multi_cloud_resource_discovery.generated import multicloudresourcediscovery_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci dbmulticloud multi-cloud-resource-discovery multi-cloud-resource-discovery' -> 'oci dbmulticloud multi-cloud-resource-discovery'
multicloudresourcediscovery_cli.multi_cloud_resource_discovery_root_group.commands.pop(multicloudresourcediscovery_cli.multi_cloud_resource_discovery_group.name)
multicloudresourcediscovery_cli.multi_cloud_resource_discovery_root_group.add_command(multicloudresourcediscovery_cli.change_multi_cloud_resource_discovery_compartment)
multicloudresourcediscovery_cli.multi_cloud_resource_discovery_root_group.add_command(multicloudresourcediscovery_cli.create_multi_cloud_resource_discovery)
multicloudresourcediscovery_cli.multi_cloud_resource_discovery_root_group.add_command(multicloudresourcediscovery_cli.delete_multi_cloud_resource_discovery)
multicloudresourcediscovery_cli.multi_cloud_resource_discovery_root_group.add_command(multicloudresourcediscovery_cli.get_multi_cloud_resource_discovery)
multicloudresourcediscovery_cli.multi_cloud_resource_discovery_root_group.add_command(multicloudresourcediscovery_cli.list_multi_cloud_resource_discoveries)
multicloudresourcediscovery_cli.multi_cloud_resource_discovery_root_group.add_command(multicloudresourcediscovery_cli.update_multi_cloud_resource_discovery)
