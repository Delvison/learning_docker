require 'httparty'
require "net/http"

class OrdersController < ApplicationController
  def index
      url = 'http://127.0.0.1:8080/api/orders'
      api_response = HTTParty.get(url)
      @all_orders = api_response.parsed_response
  end

  def new
      @random_name = ['John', 'Pablo', 'Takashi', 'Jesus','Viktor','Sally','Kim','Esther'].sample + " " + ['Ko', 'Castillo','Von Doom','Parker','Storm','Smith'].sample
      @random_order = ['quesadilla','taco','fried chicken', 'burger'].sample
      @random_total = ['$7.50','$19.20','$15.00','$11.49','$10.00',].sample
      @random_address = ["1600 Pennsylvania Ave NW, Washington, DC 20500","350 5th Ave, New York, NY 10118","
221B Baker St, Marylebone, London NW1 6XE, UK"].sample
      @random_phone = ["+1 (953) 585-3908","+1 (964) 555-3187","+1 (991) 449-3568"].sample
      @random_status = ["true","false"].sample
      @order = Order.new
  end

  def create
      @order = params[:order]
      url = 'http://127.0.0.1:8080/api/orders'
      api_response = HTTParty.post(url,
        :body => @order)
      puts api_response.body
    #  TODO: error handling
      redirect_to orders_path
  end

  def show
  end
end
