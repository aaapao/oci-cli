# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210501

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
from services.osub_subscription.src.oci_cli_osub_subscription.generated import osub_subscription_service_cli


@click.command(cli_util.override('commitment.commitment_root_group.command_name', 'commitment'), cls=CommandGroupWithAlias, help=cli_util.override('commitment.commitment_root_group.help', """Set of APIs that return the Subscription Details, Commitment and Effective Rate Card Details"""), short_help=cli_util.override('commitment.commitment_root_group.short_help', """OneSubscription API Subscription, Commitment and and Rate Card Details"""))
@cli_util.help_option_group
def commitment_root_group():
    pass


@click.command(cli_util.override('commitment.commitment_detail_group.command_name', 'commitment-detail'), cls=CommandGroupWithAlias, help="""Subscribed Service commitment summary""")
@cli_util.help_option_group
def commitment_detail_group():
    pass


@click.command(cli_util.override('commitment.commitment_group.command_name', 'commitment'), cls=CommandGroupWithAlias, help="""Subscribed service commitment details""")
@cli_util.help_option_group
def commitment_group():
    pass


osub_subscription_service_cli.osub_subscription_service_group.add_command(commitment_root_group)
commitment_root_group.add_command(commitment_detail_group)
commitment_root_group.add_command(commitment_group)


@commitment_detail_group.command(name=cli_util.override('commitment.get_commitment.command_name', 'get-commitment'), help=u"""This API returns the commitment details corresponding to the id provided \n[Command Reference](getCommitment)""")
@cli_util.option('--commitment-id', required=True, help=u"""The Commitment Id""")
@cli_util.option('--x-one-gateway-subscription-id', help=u"""This header is meant to be used only for internal purposes and will be ignored on any public request. The purpose of this header is to help on Gateway to API calls identification.""")
@cli_util.option('--x-one-origin-region', help=u"""The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'osub_subscription', 'class': 'CommitmentDetail'})
@cli_util.wrap_exceptions
def get_commitment(ctx, from_json, commitment_id, x_one_gateway_subscription_id, x_one_origin_region):

    if isinstance(commitment_id, six.string_types) and len(commitment_id.strip()) == 0:
        raise click.UsageError('Parameter --commitment-id cannot be whitespace or empty string')

    kwargs = {}
    if x_one_gateway_subscription_id is not None:
        kwargs['x_one_gateway_subscription_id'] = x_one_gateway_subscription_id
    if x_one_origin_region is not None:
        kwargs['x_one_origin_region'] = x_one_origin_region
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('osub_subscription', 'commitment', ctx)
    result = client.get_commitment(
        commitment_id=commitment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@commitment_group.command(name=cli_util.override('commitment.list_commitments.command_name', 'list'), help=u"""This list API returns all commitments for a particular Subscribed Service \n[Command Reference](listCommitments)""")
@cli_util.option('--subscribed-service-id', required=True, help=u"""This param is used to get the commitments for a particular subscribed service""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call. Default: (`50`)

Example: `500`""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "TIMESTART"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`).""")
@cli_util.option('--x-one-gateway-subscription-id', help=u"""This header is meant to be used only for internal purposes and will be ignored on any public request. The purpose of this header is to help on Gateway to API calls identification.""")
@cli_util.option('--x-one-origin-region', help=u"""The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'osub_subscription', 'class': 'list[CommitmentSummary]'})
@cli_util.wrap_exceptions
def list_commitments(ctx, from_json, all_pages, page_size, subscribed_service_id, compartment_id, limit, page, sort_order, sort_by, x_one_gateway_subscription_id, x_one_origin_region):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if x_one_gateway_subscription_id is not None:
        kwargs['x_one_gateway_subscription_id'] = x_one_gateway_subscription_id
    if x_one_origin_region is not None:
        kwargs['x_one_origin_region'] = x_one_origin_region
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('osub_subscription', 'commitment', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_commitments,
            subscribed_service_id=subscribed_service_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_commitments,
            limit,
            page_size,
            subscribed_service_id=subscribed_service_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_commitments(
            subscribed_service_id=subscribed_service_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
