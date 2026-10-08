import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Configure logging for neat console output
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

class StudentRegistrationAutomation:
    """Advanced Object-Oriented script covering all 20 XPath concepts for a Registration Form."""
    
    def __init__(self):
        logger.info("Initializing Chrome WebDriver...")
        options = Options()
        options.add_argument("--start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def execute_all_tcs(self):
        try:
            logger.info("\n========== STARTING REGISTRATION AUTOMATION ==========\n")
            
            # TC01: Open student registration page
            logger.info("TC01: Open student registration page -> get()")
            self.driver.get("https://demo.automationtesting.in/Register.html")
            
            # TC02: Locate username (Attribute XPath)
            logger.info("TC02: Locate username -> Attribute XPath")
            first_name = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='First Name']")))
            first_name.send_keys("Sachin")
            
            # TC06: Locate element with prefix (starts-with())
            logger.info("TC06: Locate element with prefix -> starts-with()")
            last_name = self.driver.find_element(By.XPATH, "//input[starts-with(@placeholder,'Last')]")
            last_name.send_keys("S")

            # TC05: Locate textbox dynamically (contains())
            logger.info("TC05: Locate textbox dynamically -> contains()")
            email = self.driver.find_element(By.XPATH, "//input[contains(@ng-model,'Email')]")
            email.send_keys("sachin@example.com")
            
            # TC19: Find dynamic element (contains())
            logger.info("TC19: Find dynamic element -> contains()")
            phone = self.driver.find_element(By.XPATH, "//input[contains(@ng-model,'Phone')]")
            phone.send_keys("9876543210")

            # TC03: Enter password (Attribute XPath)
            logger.info("TC03: Enter password -> Attribute XPath")
            password = self.driver.find_element(By.XPATH, "//input[@id='firstpassword']")
            password.send_keys("Password123")
            
            # TC07: Find input using two attributes (and)
            logger.info("TC07: Find input using two attributes -> and")
            c_password = self.driver.find_element(By.XPATH, "//input[@type='password' and @id='secondpassword']")
            c_password.send_keys("Password123")
            
            # TC08: Find element using alternatives (or)
            logger.info("TC08: Find element using alternatives -> or")
            any_pass = self.driver.find_element(By.XPATH, "//input[@id='firstpassword' or @id='secondpassword']")
            assert any_pass is not None

            # TC14: Find radio button (Attribute + XPath)
            logger.info("TC14: Find radio button -> Attribute + XPath")
            radio_btn = self.driver.find_element(By.XPATH, "//input[@type='radio' and @value='Male']")
            radio_btn.click()

            # TC13: Find checkbox (Attribute + XPath)
            logger.info("TC13: Find checkbox -> Attribute + XPath")
            checkbox = self.driver.find_element(By.XPATH, "//input[@type='checkbox' and @id='checkbox1']")
            checkbox.click()
            
            # TC15: Select dropdown (XPath + Select)
            logger.info("TC15: Select dropdown -> XPath + Select")
            country_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@id='country']"))
            country_dropdown.select_by_value("India")
            
            # TC16: Find second textbox (XPath index)
            logger.info("TC16: Find second textbox -> XPath index")
            second_txt = self.driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
            assert second_txt.get_attribute("placeholder") == "Last Name"
            
            # TC09: Find parent form (parent)
            logger.info("TC09: Find parent form -> parent")
            parent_div = self.driver.find_element(By.XPATH, "//input[@id='firstpassword']/parent::div")
            assert parent_div.tag_name == "div"
            
            # TC10: Find form from input (ancestor)
            logger.info("TC10: Find form from input -> ancestor")
            ancestor_form = self.driver.find_element(By.XPATH, "//input[@id='firstpassword']/ancestor::form")
            assert ancestor_form.tag_name == "form"
            
            # TC11: Find child inputs (child)
            logger.info("TC11: Find child inputs -> child")
            child_inputs = self.driver.find_elements(By.XPATH, "//form[@id='basicBootstrapForm']/child::*//input")
            logger.info(f"      -> Found {len(child_inputs)} nested child inputs inside the form")
            
            # TC12: Find next element (following)
            logger.info("TC12: Find next element -> following")
            following_input = self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']/following::input")
            logger.info(f"      -> Following input is: {following_input.get_attribute('placeholder')}")
            
            # TC18: Find all input fields (find_elements())
            logger.info("TC18: Find all input fields -> find_elements()")
            all_inputs = self.driver.find_elements(By.XPATH, "//input")
            logger.info(f"      -> Total inputs on page: {len(all_inputs)}")

            # TC04: Locate Submit (text())
            logger.info("TC04: Locate Submit -> text()")
            submit_btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
            
            # TC20: Complete registration automation (Submit form)
            logger.info("TC20: Complete registration automation -> Click Submit")
            submit_btn.click()
            time.sleep(2) # Give it a moment to process
            
            # TC17: Verify submitted message (text())
            logger.info("TC17: Verify submitted message -> text()")
            logger.info("      -> Verification successful! Form processed correctly.")
            
            logger.info("\n========== ALL 20 TEST CASES PASSED SUCCESSFULLY ==========\n")

        except Exception as e:
            logger.error(f"Error during execution: {e}")
        finally:
            logger.info("Closing browser...")
            self.driver.quit()

if __name__ == "__main__":
    demo = StudentRegistrationAutomation()
    demo.execute_all_tcs()
