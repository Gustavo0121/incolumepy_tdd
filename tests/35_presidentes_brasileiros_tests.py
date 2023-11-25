"""
# TODO:: Atividade 32: Do endereço https://pt.m.wikipedia.org/wiki/Lista_de_presidentes_do_Brasil, extraia as informações dos
presidentes brasileiros e grave em um arquivo chamado presidentes.json, contendo Presidente, Vice-presidente,
 Periodo do mandato e  partido político.
"""

from incolumepy.tdd import __root__
from pathlib import Path
import base64
import json
import pandas as pd
import pytest

__author__ = '@britodfbr'
path = Path(__root__) / 'src' / 'incolumepy' / 'tdd' / 'json_files'


@pytest.fixture
def content_json_presidentes():
    s = (
        'W3siUFJFU0lERU5URSI6ICJEZW9kb3JvIGRhIEZvbnNlY2EiLCAiUEFSVElETyI6IG51bGwsICJWSUNF'
        'LVBSRVNJREVOVEUiOiAiRmxvcmlhbm8gUGVpeG90byIsICJJTklDSU9fTUFOREFUTyI6ICIxNSBkZSBu'
        'b3ZlbWJybyBkZSAxODg5IiwgIkZJTV9NQU5EQVRPIjogIjIzIGRlIG5vdmVtYnJvIGRlIDE4OTEifSwg'
        'eyJQUkVTSURFTlRFIjogIkZsb3JpYW5vIFBlaXhvdG8iLCAiUEFSVElETyI6IG51bGwsICJWSUNFLVBS'
        'RVNJREVOVEUiOiBudWxsLCAiSU5JQ0lPX01BTkRBVE8iOiAiMjMgZGUgbm92ZW1icm8gZGUgMTg5MSIs'
        'ICJGSU1fTUFOREFUTyI6ICIxNSBkZSBub3ZlbWJybyBkZSAxODk0In0sIHsiUFJFU0lERU5URSI6ICJQ'
        'cnVkZW50ZSBkZSBNb3JhaXMiLCAiUEFSVElETyI6ICJQUiBGZWRlcmFsIiwgIlZJQ0UtUFJFU0lERU5U'
        'RSI6ICJNYW51ZWwgVml0b3Jpbm8iLCAiSU5JQ0lPX01BTkRBVE8iOiAiMTUgZGUgbm92ZW1icm8gZGUg'
        'MTg5NCIsICJGSU1fTUFOREFUTyI6ICIxNSBkZSBub3ZlbWJybyBkZSAxODk4In0sIHsiUFJFU0lERU5U'
        'RSI6ICJDYW1wb3MgU2FsZXMiLCAiUEFSVElETyI6ICJQUlAiLCAiVklDRS1QUkVTSURFTlRFIjogIlJv'
        'c2EgZSBTaWx2YSIsICJJTklDSU9fTUFOREFUTyI6ICIxNSBkZSBub3ZlbWJybyBkZSAxODk4IiwgIkZJ'
        'TV9NQU5EQVRPIjogIjE1IGRlIG5vdmVtYnJvIGRlIDE5MDIifSwgeyJQUkVTSURFTlRFIjogIlJvZHJp'
        'Z3VlcyBBbHZlcyIsICJQQVJUSURPIjogIlBSUCIsICJWSUNFLVBSRVNJREVOVEUiOiAiQWZvbnNvIFBl'
        'bmEiLCAiSU5JQ0lPX01BTkRBVE8iOiAiMTUgZGUgbm92ZW1icm8gZGUgMTkwMiIsICJGSU1fTUFOREFU'
        'TyI6ICIxNSBkZSBub3ZlbWJybyBkZSAxOTA2In0sIHsiUFJFU0lERU5URSI6ICJBZm9uc28gUGVuYSIs'
        'ICJQQVJUSURPIjogIlBSTSIsICJWSUNFLVBSRVNJREVOVEUiOiAiTmlsbyBQZVx1MDBlN2FuaGEiLCAi'
        'SU5JQ0lPX01BTkRBVE8iOiAiMTUgZGUgbm92ZW1icm8gZGUgMTkwNiIsICJGSU1fTUFOREFUTyI6ICIx'
        'NCBkZSBqdW5obyBkZSAxOTA5In0sIHsiUFJFU0lERU5URSI6ICJOaWxvIFBlXHUwMGU3YW5oYSIsICJQ'
        'QVJUSURPIjogIlBSRiIsICJWSUNFLVBSRVNJREVOVEUiOiBudWxsLCAiSU5JQ0lPX01BTkRBVE8iOiAi'
        'MTQgZGUganVuaG8gZGUgMTkwOSIsICJGSU1fTUFOREFUTyI6ICIxNSBkZSBub3ZlbWJybyBkZSAxOTEw'
        'In0sIHsiUFJFU0lERU5URSI6ICJIZXJtZXMgZGEgRm9uc2VjYSIsICJQQVJUSURPIjogIlBSQyIsICJW'
        'SUNFLVBSRVNJREVOVEUiOiAiVmVuY2VzbGF1IEJyXHUwMGUxcyIsICJJTklDSU9fTUFOREFUTyI6ICIx'
        'NSBkZSBub3ZlbWJybyBkZSAxOTEwIiwgIkZJTV9NQU5EQVRPIjogIjE1IGRlIG5vdmVtYnJvIGRlIDE5'
        'MTQifSwgeyJQUkVTSURFTlRFIjogIlZlbmNlc2xhdSBCclx1MDBlMXMiLCAiUEFSVElETyI6ICJQUk0i'
        'LCAiVklDRS1QUkVTSURFTlRFIjogIlVyYmFubyBTYW50b3MiLCAiSU5JQ0lPX01BTkRBVE8iOiAiMTUg'
        'ZGUgbm92ZW1icm8gZGUgMTkxNCIsICJGSU1fTUFOREFUTyI6ICIxNSBkZSBub3ZlbWJybyBkZSAxOTE4'
        'In0sIHsiUFJFU0lERU5URSI6ICJEZWxmaW0gTW9yZWlyYSIsICJQQVJUSURPIjogIlBSTSIsICJWSUNF'
        'LVBSRVNJREVOVEUiOiBudWxsLCAiSU5JQ0lPX01BTkRBVE8iOiAiMTUgZGUgbm92ZW1icm8gZGUgMTkx'
        'OCIsICJGSU1fTUFOREFUTyI6ICIyOCBkZSBqdWxobyBkZSAxOTE5In0sIHsiUFJFU0lERU5URSI6ICJF'
        'cGl0XHUwMGUxY2lvIFBlc3NvYSIsICJQQVJUSURPIjogIlBSTSIsICJWSUNFLVBSRVNJREVOVEUiOiAi'
        'QnVlbm8gZGUgUGFpdmEiLCAiSU5JQ0lPX01BTkRBVE8iOiAiMjggZGUganVsaG8gZGUgMTkxOSIsICJG'
        'SU1fTUFOREFUTyI6ICIxNSBkZSBub3ZlbWJybyBkZSAxOTIyIn0sIHsiUFJFU0lERU5URSI6ICJBcnR1'
        'ciBCZXJuYXJkZXMiLCAiUEFSVElETyI6ICJQUk0iLCAiVklDRS1QUkVTSURFTlRFIjogIkVzdFx1MDBl'
        'MWNpbyBDb2ltYnJhIiwgIklOSUNJT19NQU5EQVRPIjogIjE1IGRlIG5vdmVtYnJvIGRlIDE5MjIiLCAi'
        'RklNX01BTkRBVE8iOiAiMTUgZGUgbm92ZW1icm8gZGUgMTkyNiJ9LCB7IlBSRVNJREVOVEUiOiAiV2Fz'
        'aGluZ3RvbiBMdVx1MDBlZHMiLCAiUEFSVElETyI6ICJQUlAiLCAiVklDRS1QUkVTSURFTlRFIjogIkZl'
        'cm5hbmRvIGRlIE1lbG8gVmlhbmEiLCAiSU5JQ0lPX01BTkRBVE8iOiAiMTUgZGUgbm92ZW1icm8gZGUg'
        'MTkyNiIsICJGSU1fTUFOREFUTyI6ICIyNCBkZSBvdXR1YnJvIGRlIDE5MzAifSwgeyJQUkVTSURFTlRF'
        'IjogIkpvc1x1MDBlOSBMaW5oYXJlcyIsICJQQVJUSURPIjogbnVsbCwgIlZJQ0UtUFJFU0lERU5URSI6'
        'IG51bGwsICJJTklDSU9fTUFOREFUTyI6ICIyOSBkZSBvdXR1YnJvIGRlIDE5NDUiLCAiRklNX01BTkRB'
        'VE8iOiAiMzEgZGUgamFuZWlybyBkZSAxOTQ2In0sIHsiUFJFU0lERU5URSI6ICJFdXJpY28gR2FzcGFy'
        'IER1dHJhIiwgIlBBUlRJRE8iOiAiUFNEIiwgIlZJQ0UtUFJFU0lERU5URSI6ICJOZXJldSBSYW1vcyIs'
        'ICJJTklDSU9fTUFOREFUTyI6ICIzMSBkZSBqYW5laXJvIGRlIDE5NDYiLCAiRklNX01BTkRBVE8iOiAi'
        'MzEgZGUgamFuZWlybyBkZSAxOTUxIn0sIHsiUFJFU0lERU5URSI6ICJHZXRcdTAwZmFsaW8gVmFyZ2Fz'
        'IiwgIlBBUlRJRE8iOiAiUFRCIiwgIlZJQ0UtUFJFU0lERU5URSI6ICJDYWZcdTAwZTkgRmlsaG8iLCAi'
        'SU5JQ0lPX01BTkRBVE8iOiAiMzEgZGUgamFuZWlybyBkZSAxOTUxIiwgIkZJTV9NQU5EQVRPIjogIjI0'
        'IGRlIGFnb3N0byBkZSAxOTU0In0sIHsiUFJFU0lERU5URSI6ICJDYWZcdTAwZTkgRmlsaG8iLCAiUEFS'
        'VElETyI6ICJQU1AiLCAiVklDRS1QUkVTSURFTlRFIjogbnVsbCwgIklOSUNJT19NQU5EQVRPIjogIjI0'
        'IGRlIGFnb3N0byBkZSAxOTU0IiwgIkZJTV9NQU5EQVRPIjogIjggZGUgbm92ZW1icm8gZGUgMTk1NSJ9'
        'LCB7IlBSRVNJREVOVEUiOiAiQ2FybG9zIEx1eiIsICJQQVJUSURPIjogIlBTRCIsICJWSUNFLVBSRVNJ'
        'REVOVEUiOiBudWxsLCAiSU5JQ0lPX01BTkRBVE8iOiAiOCBkZSBub3ZlbWJybyBkZSAxOTU1IiwgIkZJ'
        'TV9NQU5EQVRPIjogIjExIGRlIG5vdmVtYnJvIGRlIDE5NTUifSwgeyJQUkVTSURFTlRFIjogIk5lcmV1'
        'IFJhbW9zIiwgIlBBUlRJRE8iOiAiUFNEIiwgIlZJQ0UtUFJFU0lERU5URSI6IG51bGwsICJJTklDSU9f'
        'TUFOREFUTyI6ICIxMSBkZSBub3ZlbWJybyBkZSAxOTU1IiwgIkZJTV9NQU5EQVRPIjogIjMxIGRlIGph'
        'bmVpcm8gZGUgMTk1NiJ9LCB7IlBSRVNJREVOVEUiOiAiSnVzY2VsaW5vIEt1Yml0c2NoZWsiLCAiUEFS'
        'VElETyI6ICJQU0QiLCAiVklDRS1QUkVTSURFTlRFIjogIkpvXHUwMGUzbyBHb3VsYXJ0IiwgIklOSUNJ'
        'T19NQU5EQVRPIjogIjMxIGRlIGphbmVpcm8gZGUgMTk1NiIsICJGSU1fTUFOREFUTyI6ICIzMSBkZSBq'
        'YW5laXJvIGRlIDE5NjEifSwgeyJQUkVTSURFTlRFIjogIkpcdTAwZTJuaW8gUXVhZHJvcyIsICJQQVJU'
        'SURPIjogIlBUTiIsICJWSUNFLVBSRVNJREVOVEUiOiAiSm9cdTAwZTNvIEdvdWxhcnQiLCAiSU5JQ0lP'
        'X01BTkRBVE8iOiAiMzEgZGUgamFuZWlybyBkZSAxOTYxIiwgIkZJTV9NQU5EQVRPIjogIjI1IGRlIGFn'
        'b3N0byBkZSAxOTYxIn0sIHsiUFJFU0lERU5URSI6ICJKb1x1MDBlM28gR291bGFydCIsICJQQVJUSURP'
        'IjogIlBUQiIsICJWSUNFLVBSRVNJREVOVEUiOiBudWxsLCAiSU5JQ0lPX01BTkRBVE8iOiAiNyBkZSBz'
        'ZXRlbWJybyBkZSAxOTYxIiwgIkZJTV9NQU5EQVRPIjogIjIgZGUgYWJyaWwgZGUgMTk2NCJ9LCB7IlBS'
        'RVNJREVOVEUiOiAiUmFuaWVyaSBNYXp6aWxsaSIsICJQQVJUSURPIjogIlBTRCIsICJWSUNFLVBSRVNJ'
        'REVOVEUiOiBudWxsLCAiSU5JQ0lPX01BTkRBVE8iOiAiMiBkZSBhYnJpbCBkZSAxOTY0IiwgIkZJTV9N'
        'QU5EQVRPIjogIjE1IGRlIGFicmlsIGRlIDE5NjQifSwgeyJQUkVTSURFTlRFIjogIkh1bWJlcnRvIENh'
        'c3RlbG8gQnJhbmNvIiwgIlBBUlRJRE8iOiAiQVJFTkEiLCAiVklDRS1QUkVTSURFTlRFIjogIkpvc1x1'
        'MDBlOSBNYXJpYSBBbGttaW4iLCAiSU5JQ0lPX01BTkRBVE8iOiAiMTUgZGUgYWJyaWwgZGUgMTk2NCIs'
        'ICJGSU1fTUFOREFUTyI6ICIxNSBkZSBtYXJcdTAwZTdvIGRlIDE5NjcifSwgeyJQUkVTSURFTlRFIjog'
        'IkFydHVyIGRhIENvc3RhIGUgU2lsdmEiLCAiUEFSVElETyI6ICJBUkVOQSIsICJWSUNFLVBSRVNJREVO'
        'VEUiOiAiUGVkcm8gQWxlaXhvIiwgIklOSUNJT19NQU5EQVRPIjogIjE1IGRlIG1hclx1MDBlN28gZGUg'
        'MTk2NyIsICJGSU1fTUFOREFUTyI6ICIzMSBkZSBhZ29zdG8gZGUgMTk2OSJ9LCB7IlBSRVNJREVOVEUi'
        'OiAiRW1cdTAwZWRsaW8gR2FycmFzdGF6dSBNXHUwMGU5ZGljaSIsICJQQVJUSURPIjogIkFSRU5BIiwg'
        'IlZJQ0UtUFJFU0lERU5URSI6ICJBdWd1c3RvIFJhZGVtYWtlciIsICJJTklDSU9fTUFOREFUTyI6ICIz'
        'MCBkZSBvdXR1YnJvIGRlIDE5NjkiLCAiRklNX01BTkRBVE8iOiAiMTUgZGUgbWFyXHUwMGU3byBkZSAx'
        'OTc0In0sIHsiUFJFU0lERU5URSI6ICJFcm5lc3RvIEdlaXNlbCIsICJQQVJUSURPIjogIkFSRU5BIiwg'
        'IlZJQ0UtUFJFU0lERU5URSI6ICJBZGFsYmVydG8gUGVyZWlyYSBkb3MgU2FudG9zIiwgIklOSUNJT19N'
        'QU5EQVRPIjogIjE1IGRlIG1hclx1MDBlN28gZGUgMTk3NCIsICJGSU1fTUFOREFUTyI6ICIxNSBkZSBt'
        'YXJcdTAwZTdvIGRlIDE5NzkifSwgeyJQUkVTSURFTlRFIjogIkpvXHUwMGUzbyBGaWd1ZWlyZWRvIiwg'
        'IlBBUlRJRE8iOiAiUERTIiwgIlZJQ0UtUFJFU0lERU5URSI6ICJBdXJlbGlhbm8gQ2hhdmVzIiwgIklO'
        'SUNJT19NQU5EQVRPIjogIjE1IGRlIG1hclx1MDBlN28gZGUgMTk3OSIsICJGSU1fTUFOREFUTyI6ICIx'
        'NSBkZSBtYXJcdTAwZTdvIGRlIDE5ODUifSwgeyJQUkVTSURFTlRFIjogIkpvc1x1MDBlOSBTYXJuZXki'
        'LCAiUEFSVElETyI6ICJQTURCIiwgIlZJQ0UtUFJFU0lERU5URSI6IG51bGwsICJJTklDSU9fTUFOREFU'
        'TyI6ICIxNSBkZSBtYXJcdTAwZTdvIGRlIDE5ODUiLCAiRklNX01BTkRBVE8iOiAiMTUgZGUgbWFyXHUw'
        'MGU3byBkZSAxOTkwIn0sIHsiUFJFU0lERU5URSI6ICJGZXJuYW5kbyBDb2xsb3IiLCAiUEFSVElETyI6'
        'ICJQUk4iLCAiVklDRS1QUkVTSURFTlRFIjogIkl0YW1hciBGcmFuY28iLCAiSU5JQ0lPX01BTkRBVE8i'
        'OiAiMTUgZGUgbWFyXHUwMGU3byBkZSAxOTkwIiwgIkZJTV9NQU5EQVRPIjogIjI5IGRlIGRlemVtYnJv'
        'IGRlIDE5OTIifSwgeyJQUkVTSURFTlRFIjogIkl0YW1hciBGcmFuY28iLCAiUEFSVElETyI6ICJQTURC'
        'IiwgIlZJQ0UtUFJFU0lERU5URSI6IG51bGwsICJJTklDSU9fTUFOREFUTyI6ICIyOSBkZSBkZXplbWJy'
        'byBkZSAxOTkyIiwgIkZJTV9NQU5EQVRPIjogIjEgZGUgamFuZWlybyBkZSAxOTk1In0sIHsiUFJFU0lE'
        'RU5URSI6ICJGZXJuYW5kbyBIZW5yaXF1ZSBDYXJkb3NvIiwgIlBBUlRJRE8iOiAiUFNEQiIsICJWSUNF'
        'LVBSRVNJREVOVEUiOiAiTWFyY28gTWFjaWVsIiwgIklOSUNJT19NQU5EQVRPIjogIjEgZGUgamFuZWly'
        'byBkZSAxOTk1IiwgIkZJTV9NQU5EQVRPIjogIjEgZGUgamFuZWlybyBkZSAyMDAzIn0sIHsiUFJFU0lE'
        'RU5URSI6ICJMdWl6IEluXHUwMGUxY2lvIEx1bGEgZGEgU2lsdmEiLCAiUEFSVElETyI6ICJQVCIsICJW'
        'SUNFLVBSRVNJREVOVEUiOiAiSm9zXHUwMGU5IEFsZW5jYXIiLCAiSU5JQ0lPX01BTkRBVE8iOiAiMSBk'
        'ZSBqYW5laXJvIGRlIDIwMDMiLCAiRklNX01BTkRBVE8iOiAiMSBkZSBqYW5laXJvIGRlIDIwMTEifSwg'
        'eyJQUkVTSURFTlRFIjogIkRpbG1hIFJvdXNzZWZmIiwgIlBBUlRJRE8iOiAiUFQiLCAiVklDRS1QUkVT'
        'SURFTlRFIjogIk1pY2hlbCBUZW1lciIsICJJTklDSU9fTUFOREFUTyI6ICIxIGRlIGphbmVpcm8gZGUg'
        'MjAxMSIsICJGSU1fTUFOREFUTyI6ICIzMSBkZSBhZ29zdG8gZGUgMjAxNiJ9LCB7IlBSRVNJREVOVEUi'
        'OiAiTWljaGVsIFRlbWVyIiwgIlBBUlRJRE8iOiAiUE1EQiIsICJWSUNFLVBSRVNJREVOVEUiOiBudWxs'
        'LCAiSU5JQ0lPX01BTkRBVE8iOiAiMzEgZGUgYWdvc3RvIGRlIDIwMTYiLCAiRklNX01BTkRBVE8iOiAi'
        'MSBkZSBqYW5laXJvIGRlIDIwMTkifSwgeyJQUkVTSURFTlRFIjogIkphaXIgQm9sc29uYXJvIiwgIlBB'
        'UlRJRE8iOiAiUFNMIiwgIlZJQ0UtUFJFU0lERU5URSI6ICJIYW1pbHRvbiBNb3VyXHUwMGUzbyIsICJJ'
        'TklDSU9fTUFOREFUTyI6ICIxIGRlIGphbmVpcm8gZGUgMjAxOSIsICJGSU1fTUFOREFUTyI6IG51bGx9'
        'XQ=='
    )
    c = base64.b64decode(s.encode('ascii', 'strict')).decode('ascii')
    return json.loads(c)


@pytest.fixture
def content_file_presidentes():
    file = path.joinpath('presidentes.json')
    return json.load(file.open())


def test_exite_path():
    assert path.exists(), f'Ops: {path} não existe.'


def test_exite_dir():
    assert path.is_dir(), f'Ops: {path} não é um diretório'


def test_json_file():
    file = path.joinpath('presidentes.json')
    assert file.exists(), f'Ops: {file}'


def test_content(content_json_presidentes, content_file_presidentes):
    df = pd.DataFrame(content_file_presidentes)
    assert df.columns.all() in [
        'PRESIDENTE',
        'PARTIDO',
        'VICE-PRESIDENTE',
        'INICIO_MANDATO',
        'FIM_MANDATO',
    ]
    assert content_json_presidentes == content_file_presidentes
