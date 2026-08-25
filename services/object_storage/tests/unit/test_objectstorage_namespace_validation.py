# Copyright (c) 2016, 2026, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at https://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.

import click
import pytest

import oci_cli.final_command_processor as final_command_processor
from services.object_storage.src.oci_cli_object_storage.generated import objectstorage_cli
from services.object_storage.src.oci_cli_object_storage.objectstorage_cli_extended import (
    NAMESPACE_VALIDATION_ERROR,
    validate_namespace_name
)


@pytest.mark.parametrize('namespace', [
    'mynamespace',
    'dex-us-phx-cli-1',
    'my_namespace',
    'my.namespace'
])
def test_validate_namespace_name_allows_host_safe_values(namespace):
    assert validate_namespace_name(namespace) == namespace


@pytest.mark.parametrize('namespace', [
    'bad/namespace',
    'bad@namespace',
    'bad?namespace',
    'bad#namespace',
    'bad:namespace',
    'bad namespace',
    ' mynamespace',
    'mynamespace ',
    '',
    ' '
])
def test_validate_namespace_name_rejects_url_unsafe_values(namespace):
    with pytest.raises(click.BadParameter) as exc:
        validate_namespace_name(namespace)

    assert NAMESPACE_VALIDATION_ERROR in str(exc.value)


def test_object_storage_namespace_callback_rejects_url_unsafe_values():
    final_command_processor.process()

    list_command = objectstorage_cli.object_group.commands['list']
    namespace_param = next(param for param in list_command.params if param.name == 'namespace')

    with pytest.raises(click.BadParameter) as exc:
        namespace_param.callback(None, namespace_param, 'bad/namespace')

    assert NAMESPACE_VALIDATION_ERROR in str(exc.value)


def test_object_storage_namespace_callback_wrapping_is_idempotent():
    final_command_processor.process()

    list_command = objectstorage_cli.object_group.commands['list']
    namespace_param = next(param for param in list_command.params if param.name == 'namespace')
    callback = namespace_param.callback

    final_command_processor.process()

    assert namespace_param.callback is callback
