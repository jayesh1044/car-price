import React from 'react';
import PropTypes from 'prop-types';
import Spinner from '../layout/Spinner';

const Price = ({ price: { price }, loading: { loading } }) => {
  return (
    <div className='card text-center'>
      {loading ? <Spinner /> : <h3>{price}</h3>}
    </div>
  );
};

Price.propTypes = {
  price: PropTypes.string.isRequired,
  loading: PropTypes.bool.isRequired,
};
export default Price;
