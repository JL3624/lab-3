# missing import statements should be added here
import wikipedia
import cv2
from matplotlib import pyplot as plt

from images import get_wikipedia_page_thumbnail_url, download_image_from_url

def prompt_for_image():
    """
    Prompts the user for the name of a Wikipedia page and obtains the URL of the thumbnail image of the page.
    
    return url, page_name: str, str
    """
    search_query = input("Enter name of a personality: ")
    try:
        
        # TODO (and remove the pass statement above)
        search_result = wikipedia.search(search_query, results = 3)
        if len(search_result) == 0:
            return None, None

        # Print out the top 3 results, and ask which user want as cartoon
        choice = 0
        choice = int(input(f"The top 3 results are : {search_result}. Which one do you want to generate for cartoon"
                       f": 1, 2 or 3?)"))
        while choice < 1 or choice > len(search_result):
            choice = int(input("Please enter a number between 1 and 3"))
            if choice < 1 or choice > len(search_result):
                print(f"Invalid choice. Please try again.")

        page_name = search_result[choice - 1]
        image_url = get_wikipedia_page_thumbnail_url(page_name)
        # return the result
        return page_name, image_url

        
    except Exception as e:
        print(f"Error: Unable to find image for the given name: {e}")
        return None, None
    
def convert_image_to_cartoon(image_path):
    """
    Converts an image to a cartoon given the image_path.
    """

    # TODO (and remove the pass statement above)

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9,9)
    color = cv2.bilateralFilter(img, 9, 200, 200)
    cartoon = cv2.bitwise_and(color, color, mask = edges)

    cv2.imwrite(image_path, cartoon)
    return image_path



if __name__ == "__main__":

    # TODO (and remove the pass statement above)

    page_name, image_url = prompt_for_image()
    image_saved_path = download_image_from_url(image_url, page_name)
    convert_image_to_cartoon(image_saved_path)

    if image_saved_path:
        cartoon_path = convert_image_to_cartoon(image_saved_path)


        # Show the cartoon image using OpenCV
        img = cv2.imread(cartoon_path)
        cv2.imshow("Cartoon Image", img)
        print(f"Cartoon image of {page_name} saved as {cartoon_path}")



