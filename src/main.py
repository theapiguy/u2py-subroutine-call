# This is a sample u2py Subroutine call Python script
import u2py
import logging

#  Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

UV_SUBROUTINE = ""
#  Create a UniVerse Subroutine that has 3 inputs, input list, output list, and error list
uv_subroutine = u2py.Subroutine(UV_SUBROUTINE, 3)

#  Set the input list
i_list = []

#  Convert the Python list to U2 Dynamic Array
uv_subroutine.args[0] = u2py.DynArray(i_list)

#  Call the UV Subroutine
uv_subroutine.call()

# Set the error list
error_list = uv_subroutine.args[2].to_list()

#  error_list[0] - 0 = Success, 1 = Error
if error_list[0] != "0":
    #  An error was encountered
    error_message = "UniVerse Error"
    logger.error(error_message)
else:
    # The Subroutine returned successfully, set the output list
    output_list = uv_subroutine.args[1].to_list()
    logger.info("UniVerse Call Successful.")

