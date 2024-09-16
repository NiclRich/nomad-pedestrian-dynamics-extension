import os.path
from logging import Logger

import pytest
from nomad.client import normalize_all, parse
from nomad.datamodel import EntryArchive


from nomad_pedestrian_dynamics_extension.nomadparserexampleMY import ExampleParserChristina


def test_parser_2():
    archive = EntryArchive()
    parser = ExampleParserChristina()
    logger = Logger("test")

    test_file = os.path.join(
        os.path.dirname(__file__), 'data', 'test.example-format.txt'
    )
    parser.parse(test_file, archive, logger)

    normalize_all(archive)

    assert archive.data.pattern.tolist() == [
        [1.0, 0.0, 1.0],
        [1.0, 1.0, 1.0],
        [1.0, 0.0, 1.0],
    ]

    print("done")

