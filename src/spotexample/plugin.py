import spot
from ocelescope import (
    Plugin,
    PluginInput,
    Resource,
    Table,
    TableColumn,
    plugin_method,
)


class EquivalanceResult(Resource):
    label = "Minimal Resource"
    description = "A minimal resource"

    form_1: str
    form_2: str

    equivalent: bool

    def visualize(self) -> Table:
        return Table(
            columns=(
                [
                    TableColumn(id="form_1", label="First Formular", data_type="string"),
                    TableColumn(id="form_2", label="Second Formular", data_type="string"),
                    TableColumn(id="result", label="Result", data_type="string"),
                ]
            ),
            rows=[
                {
                    "form_1": self.form_1,
                    "form_2": self.form_2,
                    "result": "Equivalent" if self.equivalent else "Not equivalent",
                }
            ],
        )


class Input(PluginInput):
    first_formular: str
    second_formular: str


class Spotexample(Plugin):
    label = "SpotExample"
    description = "A ocelescope plugin to test spot"
    version = "0.1.0"

    @plugin_method(label="Example Method", description="An example plugin method")
    def example(
        self,
        input: Input,
    ) -> EquivalanceResult:
        are_eq = spot.are_equivalent(input.first_formular, input.second_formular)
        return EquivalanceResult(equivalent=are_eq, form_1=input.first_formular, form_2=input.second_formular)
