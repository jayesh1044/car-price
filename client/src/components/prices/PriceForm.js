import React, { useState, useEffect, Fragment } from 'react';
import axios from 'axios';
import Spinner from '../layout/Spinner';
import Price from './Price';

const PriceForm = () => {
  const [feature, setFeature] = useState({
    car_company: '',
    car_model: '',
    car_state: '',
    car_mileage: '',
    car_year: '',
  });

  const [isSubmitted, setIsSubmitted] = useState(false);

  const [loading, setLoading] = useState(false);

  const [price, setPrice] = useState('');

  const { car_company, car_mileage, car_model, car_state, car_year } = feature;

  const onChange = (e) => {
    setFeature({ ...feature, [e.target.name]: e.target.value });
  };

  useEffect(() => {
    async function fetchMyAPI() {
      try {
        const res = await axios.post('/car/price', feature);
        setPrice({ price: res.data });
        setLoading({ loading: false });
        console.log(price);
      } catch (error) {}
    }
    if (isSubmitted) {
      fetchMyAPI();
    }
  });

  const onSubmit = (e) => {
    setIsSubmitted({ isSubmitted: true });
    setLoading({ loading: true });
    e.preventDefault();
  };

  return (
    <form onSubmit={onSubmit}>
      <h2>Enter Features</h2>
      <input
        type='text'
        placeholder='Company'
        name='car_company'
        value={car_company}
        onChange={onChange}
      />
      <input
        type='text'
        placeholder='Model'
        name='car_model'
        value={car_model}
        onChange={onChange}
      />
      <input
        type='text'
        placeholder='State'
        name='car_state'
        value={car_state}
        onChange={onChange}
      />
      <input
        type='text'
        placeholder='Mileage'
        name='car_mileage'
        value={car_mileage}
        onChange={onChange}
      />
      <input
        type='text'
        placeholder='Year'
        name='car_year'
        value={car_year}
        onChange={onChange}
      />
      <div>
        <input
          type='submit'
          value='Check Price'
          className='btn btn-primary btn-block'
        />
      </div>

      <div>
        <Price price={price} loading={loading} />
      </div>
    </form>
  );
};

export default PriceForm;
