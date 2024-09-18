from email.policy import default
from xmlrpc.client import boolean

import numpy as np
from nomad.datamodel import ArchiveSection
from nomad.datamodel.metainfo.workflow import Workflow
from nomad.metainfo import Datetime, Package, Quantity, Reference, Section, SubSection

m_package = Package(name='vadere_nomadmetainfo_json', description='None')


class PsychologyModel(ArchiveSection):

    m_def = Section()


    perception_model = Quantity(
        type=str, description="""Name of the perception model"""
    )

    cognition_model = Quantity(
        type=str, description="""Name of the cognition model"""
    )



class Model(ArchiveSection):
    m_def = Section()

    locomotion_model = Quantity(
        type=str, description="""Locomotion model"""
    )

    psychology_model = SubSection(
        sub_section=PsychologyModel, description="""Psychological model"""
    )

    time_step_size = Quantity(
        type=np.float64,
        description="""Time between two evaluations of the simulation loop.""",
        unit='s'
    )

    seed = Quantity(
        type = np.int64,
        description="""Simulation seed""",
    )

class Scenario(ArchiveSection):

    m_def = Section()

    number_of_sources = Quantity(
        type = np.int64, description="""Number of sources where agents are spawned."""
    )

    number_of_targets = Quantity(
        type=np.int64, description="""Number of targets."""
    )

    dimensions = Quantity(
        type=np.float64,
        shape=[2] ,
        description="""Outer dimension of the topography (width x height).""",
        unit='m'
    )

    origin_destination_matrix = Quantity(
        type=np.float64, shape=['number_of_sources', 'number_of_targets'], description="""Origin destination matrix."""
    )


class Output(ArchiveSection):
    m_def = Section()


    position = Quantity(
        type=np.float64,
        shape=['1...*',3],
        description="""Trajectories of the pedestrians.""",
    )


class Simulation(ArchiveSection):
    m_def = Section()

    software_name = Quantity(
        type=str, description="""Name of the software used for the simulation."""
    )

    software_release = Quantity(type=str, description="""Software release.""")

    date = Quantity(type=Datetime, description="""Start time of the execution.""")

    model = SubSection(sub_section=Model, description="""Simulation model.""")

    output = SubSection(sub_section=Output, description="""Simulation output.""")






# We extend the existing common definition of section Workflow
class ExampleWorkflow(Workflow):
    # We alter the default base class behavior to add all definitions to the existing
    # base class instead of inheriting from the base class
    m_def = Section(extends_base_section=True)

    # We define an additional example quantity. Use the prefix x_<parsername>_ to denote
    # non common quantities.
    x_example_magic_value = Quantity(
        type=int, description='The magic value from a magic source.'
    )


m_package.__init_metainfo__()