import React, { useEffect, useState, useMemo } from "react";
import { useTable } from "react-table";

const SKPTable = () => {
  const [beneficiaries, setBeneficiaries] = useState([]);

  useEffect(() => {
    (async () => {
      const axios = require("axios");
      const result = await axios.get(
        "http://127.0.0.1:8000/api/beneficiaries/"
      );
      setBeneficiaries(result.data);
    })();
  }, []);

  const cols = useMemo(
    () => [
      {
        Header: "ID",
        accessor: "id",
      },
      {
        Header: "Last Name",
        accessor: "lname",
      },
      {
        Header: "First Name",
        accessor: "fname",
      },
      {
        Header: "Middle Name",
        accessor: "mname",
      },
      {
        Header: "Contact Number",
        accessor: "mobilenum",
      },
      {
        Header: "Barangay",
        accessor: "barangay",
      },
      {
        Header: "City/Municipality",
        accessor: "city",
      },
      {
        Header: "Assistance Type",
        accessor: "assistance",
      },
      {
        Header: "Amount",
        accessor: "amount",
      },
    ],
    []
  );

  const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
    useTable({ columns: cols, data: beneficiaries });

  return (
    <div>
      <table {...getTableProps()}>
        <thead>
          {
            // Loop over the header rows
            headerGroups.map((headerGroup) => (
              // Apply the header row props
              <tr {...headerGroup.getHeaderGroupProps()}>
                {
                  // Loop over the headers in each row
                  headerGroup.headers.map((column) => (
                    // Apply the header cell props
                    <th {...column.getHeaderProps()}>
                      {
                        // Render the header
                        column.render("Header")
                      }
                    </th>
                  ))
                }
              </tr>
            ))
          }
        </thead>
        {/* Apply the table body props */}
        <tbody {...getTableBodyProps()}>
          {
            // Loop over the table rows
            rows.map((row) => {
              // Prepare the row for display
              prepareRow(row);
              return (
                // Apply the row props
                <tr {...row.getRowProps()}>
                  {
                    // Loop over the rows cells
                    row.cells.map((cell) => {
                      // Apply the cell props
                      return (
                        <td {...cell.getCellProps()}>
                          {
                            // Render the cell contents
                            cell.render("Cell")
                          }
                        </td>
                      );
                    })
                  }
                </tr>
              );
            })
          }
        </tbody>
      </table>
    </div>
  );
};
export default SKPTable;
