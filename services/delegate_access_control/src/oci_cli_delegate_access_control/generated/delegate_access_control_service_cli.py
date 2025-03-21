# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230801

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('work_request.delegate_access_control_service_group.command_name', 'delegate-access-control'), cls=CommandGroupWithAlias, help=cli_util.override('work_request.delegate_access_control_service_group.help', """Oracle Delegate Access Control allows ExaCC and ExaCS customers to delegate management of their Exadata resources operators outside their tenancies.
With Delegate Access Control, Support Providers can deliver managed services using comprehensive and robust tooling built on the OCI platform.
Customers maintain control over who has access to the delegated resources in their tenancy and what actions can be taken.
Enterprises managing resources across multiple tenants can use Delegate Access Control to streamline management tasks.
Using logging service, customers can view a near real-time audit report of all actions performed by a Service Provider operator."""), short_help=cli_util.override('work_request.delegate_access_control_service_group.short_help', """Oracle Delegate Access Control API"""))
@cli_util.help_option_group
def delegate_access_control_service_group():
    pass
