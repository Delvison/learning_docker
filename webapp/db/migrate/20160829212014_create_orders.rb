class CreateOrders < ActiveRecord::Migration
  def change
    create_table :orders do |t|
      t.string :customer
      t.string :order

      t.timestamps null: false
    end
  end
end
