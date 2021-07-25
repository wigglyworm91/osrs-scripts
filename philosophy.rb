require 'httparty'
require 'nokogiri'

domain = 'https://oldschool.runescape.wiki'


while true do
  steps = 0
  start_url = domain + '/w/Special:Random/main'

  url = start_url
  history = Array.new

  while true do
    response = HTTParty.get url, {
      headers: {'User-Agent': 'HTTParty / Wiggly'}
    }

    if response.code != 200 then
      puts 'bad response'
      break
    end

    html = Nokogiri::HTML.parse response.body

    p html.title

    if history.include? html.title then
      break
    end

    if html.at_css '.disambig' then
      puts 'Disambiguation page'
      break
    end

    history << html.title

    # extract first link
    first_link = html.css('#mw-content-text > .mw-parser-output > p a[href^="/w/"]').find { |a|
      # not image links
      a.children[0].name == "text"
    }

    if not first_link then
      puts 'No links'
      break
    end

    #p first_link[:href]

    url = domain + first_link[:href]

    sleep 1
  end

  puts "#{history.length} steps"
  puts
  sleep 2
end
