import re


class Parser:
    def __init__(self):
        pass

    def parse_telephone(self, line: str):
        __attr__ = 'TEL'

        line = line.replace(' ', '')
        telephone_type = re.findall(r'=(.*);', line)
        telephone_number = re.split(':', line)

        if telephone_type and telephone_number:
            telephone_type = telephone_type[0]  
            telephone_number = telephone_number[1]

        return telephone_type, telephone_number


    def parse_address(self):
        pass


    def parse_agent(self):
        pass


    def parse_anniversary(self):
        pass


    def parse_date_of_birth(self):
        pass


    def parse_begin(self):
        pass


    def parse_caladruri(self):
        pass


    def parse_caluri(self):
        pass


    def parse_categories(self):
        pass


    def parse_class(self):
        pass


    def parse_clientpidmap(self):
        pass


    def parse_email(self):
        pass


    def parse_end(self):
        pass


    def parse_fburl(self):
        pass


    def parse_fn(self):
        pass


    def parse_gender(self):
        pass


    def parse_geo(self):
        pass


    def parse_impp(self):
        pass


    def parse_key(self):
        pass


    def parse_kind(self):
        pass


    def parse_label(self):
        pass


    def parse_lang(self):
        pass


    def parse_logo(self):
        pass


    def parse_mailer(self):
        pass


    def parse_member(self):
        pass


    def parse_name(self):
        pass


    def parse_nickname(self):
        pass


    def parse_note(self):
        pass
    

    def parse_org(self):
        pass


    def parse_photo(self):
        pass


    def parse_prodid(self):
        pass


    def parse_profile(self):
        pass


    def parse_related(self):
        pass


    def parse_rev(self):
        pass


    def parse_role(self):
        pass


    def parse_sort_string(self):
        pass


    def parse_sound(self):
        pass


    def parse_source(self):
        pass


    def parse_title(self):
        pass

    
    def parse_timezone(self):
        pass


    def pasrse_uid(self):
        pass


    def parse_url(self):
        pass


    def parse_version(self):
        pass


    def parse_xml(self):
        pass