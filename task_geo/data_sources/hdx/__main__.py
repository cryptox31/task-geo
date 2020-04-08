from task_geo.common.datapackager import datapackage_creater
from task_geo.data_sources.hdx import hdx_acap_connector, hdx_acap_formatter


def main():
    raw, metadata, keywords = hdx_acap_connector()
    hdx_acap_formatter(raw).to_csv('Government Measures Dataset.csv')
    datapackage_creater('./Government Measures Dataset.csv', metadata, keywords)


if __name__ == '__main__':
    main()
