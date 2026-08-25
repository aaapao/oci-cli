# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest

from services.mysql.src.oci_cli_blue_green_deployments import bluegreendeployments_cli_extended  # noqa: F401
from services.mysql.src.oci_cli_blue_green_deployments.generated import bluegreendeployments_cli


class TestBlueGreenDeploymentsCliExtended(unittest.TestCase):
    def test_blue_green_deployment_help(self):
        self.assertEqual(
            'A blue/green deployment resource.',
            bluegreendeployments_cli.blue_green_deployments_root_group.help)

    def test_blue_green_deployment_short_help(self):
        self.assertEqual(
            'Manage blue/green deployments.',
            bluegreendeployments_cli.blue_green_deployments_root_group.short_help)
