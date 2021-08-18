import logging


def loggingtest():
    # 创建一个日志器
    logger = logging.getLogger()

    # 设置日志级别
    logger.setLevel(logging.INFO)

    # 创建一个格式器
    fmt = '%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
    formater = logging.Formatter(fmt)

    # 创建一个控制台处理器
    sh = logging.StreamHandler()
    # 把日志信息放到控制台
    logger.addHandler(sh)
    # 优化控制台的格式
    sh.setFormatter(formater)

    # 创建一个文本处理器
    fh = logging.FileHandler('C:/Users/xinxi/PycharmProjects/POM20210713/logs/log1.log', encoding='utf-8')
    # 把日志信息放到文本处理器
    logger.addHandler(fh)
    # 优化文本处理器设置格式
    fh.setFormatter(formater)

    # logger.info("正常")
    return logger

# loggingtest()
