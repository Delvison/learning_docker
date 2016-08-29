require 'httparty'
require "net/http"

class OrdersController < ApplicationController
  def index
      url = 'http://127.0.0.1:8080/api/orders'
      api_response = HTTParty.get(url)
      @all_orders = api_response.parsed_response
  end

  def new
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
