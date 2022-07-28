from src.driver import driver
from src.tests import triangle


def main():
    triangle.run(driver)

    driver.quit()


if __name__ == '__main__':
    main()
