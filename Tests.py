import io
from contextlib import redirect_stdout
from KitKat_Simple import kitkat_simple
from KitKat_No_Mod_Div import kitkat_no_mod_div


def validate_kitkat(fun1, func2):
    simple = io.StringIO()
    no_mod_div = io.StringIO()
    with redirect_stdout(simple):
        fun1(3, 5)
    simple_out = simple.getvalue()
    with redirect_stdout(no_mod_div):
        func2(3, 5)
    no_mod_div_out = no_mod_div.getvalue()
    assert no_mod_div_out == simple_out, "Outputs do not match"
    print("Output matches")


if __name__ == "__main__":
    validate_kitkat(kitkat_no_mod_div, kitkat_simple)
