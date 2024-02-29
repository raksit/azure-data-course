import React from "react";
import DataTable from 'react-data-table-component';

const ShopDataTable = () => {
	const columns = [
		{
			name: 'Title',
			selector: (row: { title: string; }) => row.title,
		},
		{
			name: 'Year',
			selector: (row: { year: string; }) => row.year,
		},
	];

	const data = [
		{
			id: 1,
			title: 'Beetlejuice',
			year: '1988',
		},
		{
			id: 2,
			title: 'Ghostbusters',
			year: '1984',
		},
	];

	return <DataTable columns={columns} data={data} />;
};

export default ShopDataTable;
