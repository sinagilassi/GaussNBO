# import libs
import os
from pathlib import Path
# local
from .config import (
    __version__, __author__)
from .docs import (
    NBOParser
)

def launch(file_path: Path | str, view_browser: bool = True) -> None:
    '''
    Launch to parse Gaussian NBO output file (NBO file) and display the data in a web browser.
    This function uses the NBOParser class to extract data from the NBO file and display it in a web browser.

    Parameters
    ----------
    file_path : Path | str
        path to the NBO output file or NBO file content
    view_browser : bool, optional
        If True, the extracted data will be displayed in a web browser. Default is True.

    Returns
    -------
    None

    Raises
    ------
    Exception
        If there is an error during the conversion process.
    '''
    try:
        # check
        if not file_path.endswith('.log'):
            raise Exception("Invalid file format, NBO file required!")

        # check
        if not isinstance(file_path, (str, Path)):
            raise Exception("Invalid file type, str or Path required!")
        
        # SECTION
        # check file path
        if isinstance(file_path, Path):
            # check file exist
            if not os.path.exists(file_path):
                raise Exception("File not found!, ", file_path)

        # NOTE: init NBOParser
        nbo_parser = NBOParser(file_path)
        
        # NOTE: parse data
        nob_data = nbo_parser.build_contents()
        
        # NOTE: display in a browser
        if view_browser:
            nbo_parser.display_content(nob_data)
        
        # NOTE: return data
        return nob_data
    except Exception as e:
        raise Exception("Operation failed!, ", e)