#python3 URL2Image.py 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options 
from PIL import Image
from io import BytesIO
#############################################################################################
URL = 'https://scholar.google.com/citations?user=B0fUBacAAAAJ&hl=en'
DIV_ID = 'gsc_rsb_cit'
#############################################################################################
def capture_div_as_image(url, div_id, save_path='output.png'):
    # Set up the webdriver (assuming Chrome here; can be replaced with Firefox or others)
    #options = webdriver.ChromeOptions()
    #options.headless = True  # Run in headless mode
    #browser = webdriver.Chrome(options=options)
    options = Options()
    options.add_argument("-headless")
    browser = webdriver.Firefox(options=options)
    #browser = webdriver.firefox(firefox_options=fireFoxOptions)

    # Open the URL
    browser.get(url)

    # Find the div by its ID (can be modified to search by class or other attributes)
    element = browser.find_element(By.ID,div_id)

    # Capture the element as a PNG image
    element_png = element.screenshot_as_png
    browser.quit()

    # Convert to a PIL Image and save
    image = Image.open(BytesIO(element_png))
    image.save(save_path)
    changeDimension(save_path)
    print("Screenshot saved as: "+save_path)
#############################################################################################
def changeDimension(save_path):
    with Image.open(save_path) as img:
        new_dimensions = (200, 100)  # Change this to your desired dimensions
        resized_img = img.resize(new_dimensions, Image.ANTIALIAS)
        resized_img.save(save_path)
#############################################################################################
capture_div_as_image(URL, DIV_ID, save_path="GoogleScholarCitation.png")
