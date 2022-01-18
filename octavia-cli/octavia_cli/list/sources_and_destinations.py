#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#

from typing import Callable

import airbyte_api_client
from airbyte_api_client.api import destination_api, source_api

from .base import BaseListing, DefinitionType


class SourcesAndDestinations(BaseListing):
    def __init__(self, api_client: airbyte_api_client.ApiClient, workspace_id: str):
        self.workspace_id = workspace_id
        super().__init__(api_client)

    @property
    def request_body(self) -> dict:
        return {"workspace_id": self.workspace_id}


class Sources(SourcesAndDestinations):
    definition_type = DefinitionType.SOURCE
    api = source_api.SourceApi
    list_field_in_response = "sources"
    fields_to_display = ["name", "sourceName", "sourceId"]

    def get_list_fn(self) -> Callable:
        return self.api.list_sources_for_workspace


class Destinations(SourcesAndDestinations):
    definition_type = DefinitionType.DESTINATION
    api = destination_api.DestinationApi
    list_field_in_response = "destinations"
    fields_to_display = ["name", "destinationName", "destinationId"]

    def get_list_fn(self) -> Callable:
        return self.api.list_destinations_for_workspace
