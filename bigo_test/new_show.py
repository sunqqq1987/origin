
from scrapy import cmdline


def generate_spider_cmd(name):
    cmd = "scrapy crawl {name}".format(name=name)
    return cmd


def main():

    print("bigo区域信息获取中------------------")
    # cmdline.execute(generate_spider_cmd("zy_course_list").split())
    cmdline.execute(generate_spider_cmd("bigo_show_new").split())

# ershou_viewer
if __name__ == "__main__":
    main()
