import scrapy


class BulldogJobSpider(scrapy.Spider):
    name = "bulldog"
    allowed_domains = ['bulldogjob.pl']

    roles = dict(
        backend='Backend',
        analyst='Analityk',
        devops='DevOps',
        frontend='Frontend',
        fullstack='Full-stack',
        administrator='Administrator',
        project_manager='Project Manager',
        qa='QA',
        tester='Tester',
        mobile='Mobile',
        architect='Architekt',
        support='Support',
        tech_lead='Tech Lead',
        embedded='Embedded',
        scrum_master='Scrum Master',
        security='Bezpieczeństwo',
        designer='UX/UI designer',
        gamedev='GameDev',
        data='Data Science/Engineering',
        consultant='Konsultant IT'
    )

    start_urls = [f'https://bulldogjob.pl/companies/jobs/s/role,{role}' for role in list(roles)]

    def parse(self, response, page=1, role=None):
        role = role if role else self.roles.get(response.url.split(',')[-1])

        offers = response.xpath('//div[@class="container"]//a/@href').getall()
        if len(offers) > 0:
            for offer in offers:
                yield response.follow(offer, self.parse_offer, cb_kwargs=dict(role=role))
            next_page = f'{response.url.split("/page")[0]}/page,{page + 1}'
            yield response.follow(next_page, self.parse, cb_kwargs=dict(page=page+1, role=role))

    def parse_offer(self, response, role=None):
        stack = response.xpath('//span[@class="pr-3 font-medium overflow-hidden overflow-ellipsis"]//text()').getall()
        if len(stack) > 0:
            return dict(role=role, stack=stack)
