import React from "react";
import DataTable from 'react-data-table-component';

//  Internally, customStyles will deep merges your customStyles with the default styling.
const customStyles = {

	head: {
		style: {
			fontSize: '1.25rem',
		},
	},
	cells: {
		style: {
			fontSize: '0.9rem',
		},
	}

};

const ShopDataTable = () => {
	const columns = [
		{
			name: 'Title',
			selector: (row: { title: string; }) => row.title,
			sortable: true,

		},
		{
			name: 'Year',
			selector: (row: { year: string; }) => row.year,
			sortable: true,

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

	return <DataTable
		columns={columns}
		data={data}

		customStyles={customStyles}
	/>;
};

export default ShopDataTable;
