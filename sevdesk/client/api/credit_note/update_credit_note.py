from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.credit_note import CreditNote
from ...models.update_credit_note_response_200 import UpdateCreditNoteResponse200
from ...types import Response


def _get_kwargs(
    document_id: int,
    *,
    client: Client,
    json_body: CreditNote,
) -> Dict[str, Any]:
    url = "{}/CreditNote/{DocumentId}".format(client.base_url, DocumentId=document_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, UpdateCreditNoteResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateCreditNoteResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, UpdateCreditNoteResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    document_id: int,
    *,
    client: Client,
    json_body: CreditNote,
) -> Response[Union[Any, UpdateCreditNoteResponse200]]:
    """Update an existing Credit Note

     Update an Credit Note

    Args:
        document_id (int):
        json_body (CreditNote):

    Returns:
        Response[Union[Any, UpdateCreditNoteResponse200]]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    document_id: int,
    *,
    client: Client,
    json_body: CreditNote,
) -> Optional[Union[Any, UpdateCreditNoteResponse200]]:
    """Update an existing Credit Note

     Update an Credit Note

    Args:
        document_id (int):
        json_body (CreditNote):

    Returns:
        Response[Union[Any, UpdateCreditNoteResponse200]]
    """

    return sync_detailed(
        document_id=document_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    document_id: int,
    *,
    client: Client,
    json_body: CreditNote,
) -> Response[Union[Any, UpdateCreditNoteResponse200]]:
    """Update an existing Credit Note

     Update an Credit Note

    Args:
        document_id (int):
        json_body (CreditNote):

    Returns:
        Response[Union[Any, UpdateCreditNoteResponse200]]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    document_id: int,
    *,
    client: Client,
    json_body: CreditNote,
) -> Optional[Union[Any, UpdateCreditNoteResponse200]]:
    """Update an existing Credit Note

     Update an Credit Note

    Args:
        document_id (int):
        json_body (CreditNote):

    Returns:
        Response[Union[Any, UpdateCreditNoteResponse200]]
    """

    return (
        await asyncio_detailed(
            document_id=document_id,
            client=client,
            json_body=json_body,
        )
    ).parsed