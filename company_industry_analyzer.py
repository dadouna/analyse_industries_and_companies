'''
Author Mona Dadoun
Date 2017-11-29
'''

import csv
from html2text import html2text
import urllib.request


def parse_industries(industries_data_file_name, key):
    with open(industries_data_file_name, encoding='utf-8') as f:
        csv_file = csv.reader(f, delimiter=';')
        industry_code = {}
        industry_names = {}

        for row in csv_file:
            for i in range(len(row)):
                row[i] = row[i].strip().lower()

            industry_name = row[1]
            industry_parent_name = row[2]
            if industry_parent_name:
                industry_name = industry_name + ', ' + industry_parent_name

            industry_code.update({str(row[key]): set(row[1:])})
            industry_names.update({str(row[key]): industry_name})
        return industry_code, industry_names


def parse_companies(companies_data_file_name):
    with open(companies_data_file_name, encoding='utf-8') as f:
        csv_file = csv.reader(f, delimiter=';')
        url_list = []
        for row in csv_file:
            url = row[8]
            if url != '':
                if not url.startswith('http'):
                    url = 'http://' + url

            url_list.append(url)

        return url_list


def read_text_from_url(url):
    website = None
    try:
        website = urllib.request.urlopen(url)
        website_bytes = website.read()
        html = website_bytes.decode("utf8")
        text = html2text(html)
    except:
        return
    finally:
        if website:
            website.close()
    return text


def analyze_keywords(all_key_words, industries_dict):
    best_industry_code = None
    max_matched_words = 0
    best_matched_words = set()
    for industry_code, industry_key_words in industries_dict.items():
        matched_words = set()
        for word in all_key_words:
            if len(word) > 3 and not (word.isdigit()):
                if industry_key_words.__contains__(word):
                    matched_words.add(word)

        if max_matched_words < len(matched_words):
            max_matched_words = len(matched_words)
            best_industry_code = industry_code
            best_matched_words = matched_words

    return best_industry_code, best_matched_words


def main():
    industries_data_file_name = 'industry_data.csv'
    companies_data_file_name = 'company_data.csv'
    industries_dict, industry_names = parse_industries(industries_data_file_name, 0)
    url_list = parse_companies(companies_data_file_name)
    print(url_list)
    for url in url_list:
        html_string = read_text_from_url(url)
        if html_string is not None:
            all_key_words = html_string.lower().split()
            best_industry_code, best_matched_words = analyze_keywords(all_key_words, industries_dict)
            print("URL: " + str(url))
            print("Best industry code is: " + str(best_industry_code))
            print("Best matched words" + str(best_matched_words))
            print(industry_names.get(best_industry_code))

main()

