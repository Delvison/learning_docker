class CreateOrders < ActiveRecord::Migration
  def change
    create_table :orders do |t|
      t.string :customer
      t.string :order
      t.boolean :isFulfilled
      t.string :total
      t.string :phone
      t.string :adress

      t.timestamps null: false
    end
  end
end
