from PIL import Image

from scraper.image_scraper import ImageScrapper
from scraper.user_agent import UserAgent

IMAGE_FORMAT = '.png'  # Change the image type of saved image
URL = 'https://cdn.fileinfo.com/img/ss/lg/jpg_44.jpg'  # Image url which needs to be downloaded
HTTP_PROXY = 'http://188.68.56.248:3128'  # http Proxy ip with port
HTTPS_PROXY = 'https://188.68.56.248:3128'
IMAGE_DIR= 'image/'

agents = UserAgent().get_random_user_agent()

headers = {'User-Agent': agents,
           'Cache-Control': 'no-cache',
           'Accept-Language': 'en-US,en;q=0.5',
           'Upgrade-Insecure-Requests': '1',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Pragma': 'no-cache'
           }
if __name__ == '__main__':
    proxies = dict(http=HTTP_PROXY, https=HTTPS_PROXY)

    scraper = ImageScrapper(url=URL, proxies=proxies, headers=headers)

    response = scraper.scrap()

  # If we don't get successful response
    if response.status_code == 200:

        # Getting file name from the image url
        file_name = URL.split('/')[-1].split('.')[0]+IMAGE_FORMAT

        # Generating image file from response
        open(file_name, "wb+").write(response.content)

        # Getting image object
        image = Image.open(file_name)

        # If, we have image object then...
        if image:
            print('Image Downloaded Successfully')