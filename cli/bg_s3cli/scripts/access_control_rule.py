#
# Copyright 2016 BloomReach, Inc.
# Copyright 2016 Ronak Kothari <ronak.kothari@gmail.com>.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from module_rule import ModuleRule
from utils import module_rule_utils

class AccessControlRule(ModuleRule):
  """
  Defines Rule object for Access Module
  """
  access = "access"

  def __init__(self, rule_data):
    self.rule_data = rule_data

  def build(self):
    """
    Returns the rule object for Access Control Module
    """
    rule = {}
    rule[ModuleRule.key] = self.rule_data[module_rule_utils.rule_key]
    rule[ModuleRule.value] = self.rule_data[module_rule_utils.rule_value]
    rule[ModuleRule.type] = self.rule_data[module_rule_utils.rule_type]
    rule[ModuleRule.api] = self.rule_data[module_rule_utils.rule_uri]
    rule[AccessControlRule.access] = self.rule_data[module_rule_utils.rule_access]

    return rule
