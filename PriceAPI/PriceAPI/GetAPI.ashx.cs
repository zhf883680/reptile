using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Newtonsoft.Json;

namespace PriceAPI
{
    /// <summary>
    /// GetAPI 的摘要说明
    /// </summary>
    public class GetAPI : IHttpHandler
    {

        public void ProcessRequest(HttpContext context)
        {
            context.Response.ContentType = "text/plain";
            Models.jdEntities db = new Models.jdEntities();
            if (context.Request.HttpMethod.ToLower() == "post")
            {
                switch (context.Request.Form["action"])
                {
                    case "get":
                        {
                            int id = 0;
                            int.TryParse(context.Request.Form["id"], out id);
                            //获取数据
                            var shopInfo = db.shop.Where(a => a.id == id).FirstOrDefault();
                            if (shopInfo == null)
                            {
                                //增加该数据
                                db.shop.Add(new Models.shop() { isSelf = 1, id = id, name = "", businessman = "" });
                                db.SaveChanges();
                                //执行python

                                context.Response.Write("{\"result\":\"-1\"}");
                                context.Response.End();
                            }
                            //获取该数据的价格
                            var prices = db.price.Where(a => a.shopId == id).ToList();
                            if (prices.Count == 0)
                            {
                                //没有价格记录
                                context.Response.Write("{\"result\":\"-2\"}");
                                context.Response.End();
                            }
                            //将数据转换成json后传回
                            var model = new Models.returnJson() { name = shopInfo.name, prices = prices };
                            context.Response.Write(JsonConvert.SerializeObject(model));
                            context.Response.End();
                        }break;

                }
            }
        }

        public bool IsReusable
        {
            get
            {
                return false;
            }
        }
    }
}