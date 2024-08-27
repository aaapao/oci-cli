# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230801

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.delegate_access_control import DelegateAccessControlClient

MODULE_TO_TYPE_MAPPINGS["delegate_access_control"] = oci.delegate_access_control.models.delegate_access_control_type_mapping
if CLIENT_MAP.get("delegate_access_control") is None:
    CLIENT_MAP["delegate_access_control"] = {}
CLIENT_MAP["delegate_access_control"]["delegate_access_control"] = DelegateAccessControlClient
