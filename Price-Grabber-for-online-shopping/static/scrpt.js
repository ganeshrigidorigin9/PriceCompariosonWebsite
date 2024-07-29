function validname(){
    let ipname;
    ipname = document.getElementById("ip").value;
        if(ipname=="NA" || ipname=="Na" || ipname=="na" || ipname=='')
        {
            window.alert("Enter valid Name")
        }
    }
    function removeRows() {
        var table = document.getElementById("myTable");
        var rows = table.getElementsByTagName("tr");
        for (var i = rows.length - 1; i >= 0; i--) {
            var cells = rows[i].getElementsByTagName("td");
            for (var j = 0; j < cells.length; j++) {
                if (cells[j].textContent.trim() === "NA") {
                    table.deleteRow(i);
                    break; // Once a "NA" is found in a row, remove the row and move to the next row.
                }
            }
        }
        var dollar_amount=document.getElementById("doll").textContent;
        var dollar_amount_float=parseFloat(dollar_amount)
        var rupee=dollar_amount_float*83.245;
        document.getElementById("doll").textContent="₹"+parseInt(rupee);

    }
