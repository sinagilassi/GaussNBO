# NBO PARSER
# ------------------------------------------
# import libs
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import webbrowser
import tempfile
# local
from .nbo_analysis import NBOAnalysis
from ..parsers import parser_naoo
from ..parsers import parser_npa
from ..parsers import parser_nba
from ..parsers import parser_o
from ..parsers import parser_d
from ..parsers import parser_sop
from ..parsers import parser_nbos


class NBOParser(NBOAnalysis):
    """
    A class to parse NBO output files generated by Gaussian.
    """

    def __init__(self, file_path: Path | str):
        """
        Initialize the NBOParser with a file path.

        Parameters
        ----------
        file_path : str
            The path to the NBO output file.
        """
        super().__init__(file_path)
        self.file_path = file_path

    def parse_natural_atomic_orbital_occupancies(self):
        """Parse natural atomic orbital occupancies from the NBO output file."""
        try:
            # content
            content_ = self.content_retriever(
                self.NATURAL_ATOMIC_ORBITAL_ACCUPACIES)

            # check
            if not content_:
                raise ValueError(
                    "No content found for natural atomic orbital occupancies.")

            # parse the content
            parsed_data = parser_naoo(content_[0])

            # res
            return parsed_data
        except Exception as e:
            raise Exception(
                f"Error parsing natural atomic orbital occupancies: {e}")

    def parse_natural_population_analysis(self):
        """Parse natural population analysis from the NBO output file."""
        try:
            # content
            content_ = self.content_retriever(
                self.SUMMARY_OF_NATURAL_POPULATION_ANALYSIS)

            # check
            if not content_:
                raise ValueError(
                    "No content found for natural population analysis.")

            # parse the content
            parsed_data = parser_npa(content_[0])

            # res
            return parsed_data
        except Exception as e:
            raise Exception(f"Error parsing natural population analysis: {e}")

    def parse_summary_natural_bond_orbital_analysis(self):
        """Parse summary natural bond orbital analysis from the NBO output file."""
        try:
            # content
            content_ = self.content_retriever(
                self.NATURAL_BOND_ORBITAL_ANALYSIS)

            # check
            if not content_:
                raise ValueError(
                    "No content found for natural bond orbital analysis.")

            # parse the content
            parsed_data = parser_nba(content_[0])

            # res
            return parsed_data
        except Exception as e:
            raise Exception(
                f"Error parsing natural bond orbital analysis: {e}")

    def parse_bond_orbital_coefficients_hybrids(self):
        """Parse bond orbital coefficients and hybrids from the NBO output file."""
        try:
            # content
            content_ = self.content_retriever(
                self.BOND_ORBITAL_COEFFICIENTS_HYBRIDS)

            # check
            if not content_:
                raise ValueError("No content found for bond orbital analysis.")

            # parse the content
            parsed_data = parser_o(content_[0])

            # res
            return parsed_data
        except Exception as e:
            raise Exception(
                f"Error parsing bond orbital coefficients & hybrids: {e}")

    def parse_nho_directionality(self):
        """Parse NHO directionality from the NBO output file."""
        try:
            # content
            content_ = self.content_retriever(
                self.NHO_DIRECTIONALITY_BOND_BENDING)

            # check
            if not content_:
                raise ValueError("No content found for NHO directionality.")

            # parse the content
            parsed_data = parser_d(content_[0])

            # res
            return parsed_data
        except Exception as e:
            raise Exception(f"Error parsing NHO directionality: {e}")

    def parse_second_order_perturbation(self):
        """Parse second order perturbation from the NBO output file."""
        try:
            # content
            content_ = self.content_retriever(
                self.SECOND_ORDER_PERTURBATION_THEORY_ANALYSIS)

            # check
            if not content_:
                raise ValueError(
                    "No content found for second order perturbation.")

            # parse the content
            parsed_data = parser_sop(content_[1])

            # res
            return parsed_data
        except Exception as e:
            raise Exception(f"Error parsing second order perturbation: {e}")

    def parse_natural_bond_orbital_summary(self):
        """Parse natural bond orbital summary from the NBO output file."""
        try:
            # content
            content_ = self.content_retriever(
                self.NATURAL_BOND_ORBITALS_SUMMARY)

            # check
            if not content_:
                raise ValueError(
                    "No content found for natural bond orbital summary.")

            # parse the content
            parsed_data = parser_nbos(content_[0])

            # res
            return parsed_data
        except Exception as e:
            raise Exception(f"Error parsing natural bond orbital summary: {e}")

    def build_contents(self):
        """
        Build contents for all sections.

        Returns
        -------
        dict
            A dictionary containing the contents.
        """
        try:
            # content
            content = {
                self.NATURAL_ATOMIC_ORBITAL_ACCUPACIES: self.parse_natural_atomic_orbital_occupancies(),
                self.SUMMARY_OF_NATURAL_POPULATION_ANALYSIS: self.parse_natural_population_analysis(),
                self.NATURAL_BOND_ORBITAL_ANALYSIS: self.parse_summary_natural_bond_orbital_analysis(),
                self.BOND_ORBITAL_COEFFICIENTS_HYBRIDS: self.parse_bond_orbital_coefficients_hybrids(),
                self.NHO_DIRECTIONALITY_BOND_BENDING: self.parse_nho_directionality(),
                self.SECOND_ORDER_PERTURBATION_THEORY_ANALYSIS: self.parse_second_order_perturbation(),
                self.NATURAL_BOND_ORBITALS_SUMMARY: self.parse_natural_bond_orbital_summary()
            }

            # res
            return content
        except Exception as e:
            raise Exception(f"Error building contents: {e}")

    def display_in_browser(self):
        """
        Display contents for all sections in a browser.
        """
        try:
            def generate_html_template(data):
                '''Generate HTML template from data.'''
                # source path (relative to the current file's location)
                source_path = Path(__file__).resolve().parent.parent
                # template path (relative to the source path)
                template_path = source_path / 'templates'
                # check path
                if not template_path.exists():
                    raise FileNotFoundError(
                        f"Template path {template_path} does not exist.")

                # check template
                template_file = template_path / 'nbo.html'
                if not template_file.exists():
                    raise FileNotFoundError(
                        f"Template file {template_file} does not exist.")

                # load template
                env = Environment(loader=FileSystemLoader(template_path))
                # check template
                if not env:
                    raise FileNotFoundError(
                        f"Template environment could not be loaded.")

                # check template
                template = env.get_template('nbo.html')
                if not template:
                    raise FileNotFoundError(
                        f"Template file {template_file} could not be loaded.")

                # render template
                return template.render(data=data)

            def save_and_open_html(data):
                html_content = generate_html_template(data)
                with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as temp_file:
                    temp_file.write(html_content)
                    webbrowser.open(temp_file.name)

            # content
            contents = self.build_contents()

            # display
            save_and_open_html(contents)

        except Exception as e:
            raise Exception(f"Error displaying contents: {e}")

    def create_webapp(self, data):
        """
        Initialize the web application with the given data.
        
        Parameters
        ----------
        data : dict
            The data to be displayed in the web application.
            
        Returns
        -------
        None
        
        Raises
        ------
        Exception
            If there is an error during the initialization process.
        
        Notes
        -----
        This method generates an HTML template from the provided data and opens it in a web browser.
        The HTML template is loaded from a file located in the 'templates' directory relative to the current file's location.
        """
        try:
            def generate_html_template(data):
                '''Generate HTML template from data.'''
                # source path (relative to the current file's location)
                source_path = Path(__file__).resolve().parent.parent
                # template path (relative to the source path)
                template_path = source_path / 'templates'
                # check path
                if not template_path.exists():
                    raise FileNotFoundError(
                        f"Template path {template_path} does not exist.")

                # check template
                template_file = template_path / 'nbo.html'
                if not template_file.exists():
                    raise FileNotFoundError(
                        f"Template file {template_file} does not exist.")

                # load template
                env = Environment(loader=FileSystemLoader(template_path))
                # check template
                if not env:
                    raise FileNotFoundError(
                        f"Template environment could not be loaded.")

                # check template
                template = env.get_template('nbo.html')
                if not template:
                    raise FileNotFoundError(
                        f"Template file {template_file} could not be loaded.")

                # render template
                return template.render(data=data)

            def save_and_open_html(data):
                html_content = generate_html_template(data)
                with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as temp_file:
                    temp_file.write(html_content)
                    webbrowser.open(temp_file.name)
                    
            # content
            save_and_open_html(data)
        except Exception as e:
            raise Exception(f"Error initializing webapp: {e}")

    def display_content(self, content: dict):
        """
        Display a specific content section in a browser.

        Parameters
        ----------
        content : str
            The content section to display.
        """
        try:
            # check content
            if not content:
                raise ValueError("No content found.")

            # create webapp
            self.create_webapp(content)

        except Exception as e:
            raise Exception(f"Error displaying content: {e}")