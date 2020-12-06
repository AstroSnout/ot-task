import React, { useState, useEffect } from 'react';
import Table from 'react-bootstrap/Table';
import ContentTableRow from './ContentTableRow';

const ContentTable = (props) => {
  return (
    <Table striped bordered hover>
        <thead>
            <tr>
                <th>Tx Hash</th>
                <th>From</th>
                <th>To</th>
                <th>Timestamp</th>
                <th>Value in ETH</th>
                <th>Gas Used</th>
            </tr>
        </thead>
        <tbody>
            {props.data.map((tx, i) => (
                <ContentTableRow key={i}
                    txhash={tx.hash}
                    from={tx.sender}
                    to={tx.receiver}
                    blockNo={tx.block_number}
                    value={tx.value}
                    gasUsed={tx.gas_used}
                />
            ))}
        </tbody>
    </Table>
  );
}

export default ContentTable;