# import libs
import GaussNBO as gnbo
from rich import print

# version
print(gnbo.__version__)
# author
print(gnbo.__author__)

# extract data
nbo_data = gnbo.launch(
    file_path=r'E:\Python Projects\GaussNBO\tests\nbo.log',
    view_browser=False
)
print(nbo_data)