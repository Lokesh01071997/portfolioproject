use projectportfolio;

show tables;
select*from supermarket_sales;

-- Which branch has the best results in the loyalty program?
 
 select branch, city, customer_type, rating
 from supermarket_sales;
--  branch C has the best results in the loyalty program

 select branch, city, customer_type, rating
 from supermarket_sales
 where customer_type = "Member" and rating>9
 order by rating desc 
 
 
 -- Does the membership depend on customer rating?
 
 select s1.branch, s1.customer_type, s1.rating, s2.customer_type, s2.rating
 from supermarket_sales as s1, supermarket_sales s2
 where s1.customer_type= "member" and s1.rating>9.5 and s2.customer_type = "normal" and s2.rating>9.5
 order by s1.rating desc, s2.rating desc;
 -- it is clear that membership does not depend on customer rating
 
-- Does gross income depend on the proportion of customers in the loyalty program? On payment method?

select s1.invoice_id , s1.customer_type as "member", s1.gross_income, s1.payment, s2.customer_type as "not a member", s2.gross_income, s2.payment, s2.invoice_id
from supermarket_sales as s1 , supermarket_sales s2
where s1.customer_type= "member"  and  s2.customer_type = "normal"
group by s1.gross_income, s1.payment, s1.Invoice_ID, s2.gross_income, s2.Payment, s2.Invoice_ID;


select*from supermarket_sales;


 select  customer_type, sum(gross_income)
 from supermarket_sales
 where Customer_type = "member";

 select  customer_type, sum(gross_income)
 from supermarket_sales
 where Customer_type = "normal" ;
 
  select  customer_type, sum(gross_income)
 from supermarket_sales
 where Customer_type = "member" and gross_income>40 ;
 
  select  customer_type, sum(gross_income)
 from supermarket_sales
 where Customer_type = "normal" and gross_income>40 ;

 
 select  customer_type, sum(gross_income) ,payment
 from supermarket_sales
 where Customer_type = "member" and gross_income>40 
 group by Customer_type, Payment;

select  customer_type, sum(gross_income) ,payment
 from supermarket_sales
 where Customer_type = "normal" and gross_income>40 
 group by Customer_type, Payment;

 select customer_type, gross_income, payment, count(branch) over (partition by Branch) as total_branch
 from supermarket_sales
 where Customer_type = "normal" and gross_income>45 ;
 
  -- YES gross income depends on the proportion of customers in the loyalty program 
 -- but gross income does not depends on the proportion of payment method
 
-- Are there any differences in indicators between men and women?
select*from supermarket_sales;

select gender, sum(gross_income)
from supermarket_sales
where Customer_type = "member"
group by Gender;

select gender, sum(gross_income)
from supermarket_sales
where Customer_type = "normal"
group by Gender;

-- Female customers generates more gross income than male customers


-- Which product category generates the highest income?
select product_line, sum(gross_income)
from supermarket_sales
group by Product_line
order by sum(gross_income)desc;

-- food and beverages generates the highest income

