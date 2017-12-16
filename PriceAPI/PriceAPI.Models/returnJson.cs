using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PriceAPI.Models
{
   public class returnJson
    {
        public string name { get; set; }
        public List<price> prices{ get; set; }
    }
}
