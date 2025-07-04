# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240501

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.dbmulticloud.src.oci_cli_dbmulticloud.generated import dbmulticloud_service_cli


@click.command(cli_util.override('oracle_db_azure_key.oracle_db_azure_key_root_group.command_name', 'oracle-db-azure-key'), cls=CommandGroupWithAlias, help=cli_util.override('oracle_db_azure_key.oracle_db_azure_key_root_group.help', """1. Oracle Azure Connector Resource: This is for installing Azure Arc Server in ExaCS VM Cluster.
  There are two way to install Azure Arc Server (Azure Identity) in ExaCS VMCluster.
    a. Using Bearer Access Token or
    b. By providing Authentication token

2. Oracle Azure Blob Container Resource: This is for to capture Azure Container details
   and same will be used in multiple ExaCS VMCluster to mount the Azure Container.

3. Oracle Azure Blob Mount Resource: This is for to mount Azure Container in ExaCS VMCluster
   using Oracle Azure Connector and Oracle Azure Blob Container Resource."""), short_help=cli_util.override('oracle_db_azure_key.oracle_db_azure_key_root_group.short_help', """Oracle Database MultiCloud Data plane Integration"""))
@cli_util.help_option_group
def oracle_db_azure_key_root_group():
    pass


@click.command(cli_util.override('oracle_db_azure_key.oracle_db_azure_key_group.command_name', 'oracle-db-azure-key'), cls=CommandGroupWithAlias, help="""Oracle DB Azure Key Resource Object.""")
@cli_util.help_option_group
def oracle_db_azure_key_group():
    pass


dbmulticloud_service_cli.dbmulticloud_service_group.add_command(oracle_db_azure_key_root_group)
oracle_db_azure_key_root_group.add_command(oracle_db_azure_key_group)


@oracle_db_azure_key_group.command(name=cli_util.override('oracle_db_azure_key.get_oracle_db_azure_key.command_name', 'get'), help=u"""Get Oracle DB Azure Key Details form a particular Container Resource ID. \n[Command Reference](getOracleDbAzureKey)""")
@cli_util.option('--oracle-db-azure-key-id', required=True, help=u"""The [OCID] of the Oracle DB Azure Vault Key Resource.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dbmulticloud', 'class': 'OracleDbAzureKey'})
@cli_util.wrap_exceptions
def get_oracle_db_azure_key(ctx, from_json, oracle_db_azure_key_id, limit, page, sort_order):

    if isinstance(oracle_db_azure_key_id, six.string_types) and len(oracle_db_azure_key_id.strip()) == 0:
        raise click.UsageError('Parameter --oracle-db-azure-key-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dbmulticloud', 'oracle_db_azure_key', ctx)
    result = client.get_oracle_db_azure_key(
        oracle_db_azure_key_id=oracle_db_azure_key_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@oracle_db_azure_key_group.command(name=cli_util.override('oracle_db_azure_key.list_oracle_db_azure_keys.command_name', 'list'), help=u"""Lists the all Oracle DB Azure Keys based on filters. \n[Command Reference](listOracleDbAzureKeys)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [ID] of the compartment.""")
@cli_util.option('--display-name', help=u"""A filter to return Azure Vault Keys.""")
@cli_util.option('--oracle-db-azure-vault-id', help=u"""A filter to return Oracle DB Azure Vault Resources.""")
@cli_util.option('--oracle-db-azure-key-id', help=u"""A filter to return Oracle DB Azure Vault Key Resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources that match the given lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified, default is timeCreated.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dbmulticloud', 'class': 'OracleDbAzureKeySummaryCollection'})
@cli_util.wrap_exceptions
def list_oracle_db_azure_keys(ctx, from_json, all_pages, page_size, compartment_id, display_name, oracle_db_azure_vault_id, oracle_db_azure_key_id, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if oracle_db_azure_vault_id is not None:
        kwargs['oracle_db_azure_vault_id'] = oracle_db_azure_vault_id
    if oracle_db_azure_key_id is not None:
        kwargs['oracle_db_azure_key_id'] = oracle_db_azure_key_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dbmulticloud', 'oracle_db_azure_key', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_oracle_db_azure_keys,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_oracle_db_azure_keys,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_oracle_db_azure_keys(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
