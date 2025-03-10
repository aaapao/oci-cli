# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240815

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.security_attribute import SecurityAttributeClient

MODULE_TO_TYPE_MAPPINGS["security_attribute"] = oci.security_attribute.models.security_attribute_type_mapping
if CLIENT_MAP.get("security_attribute") is None:
    CLIENT_MAP["security_attribute"] = {}
CLIENT_MAP["security_attribute"]["security_attribute"] = SecurityAttributeClient
