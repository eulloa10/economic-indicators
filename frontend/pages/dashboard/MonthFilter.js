import styles from '../../styles/Dashboard/MonthFilter.module.css';

function MonthFilter() {
  return (
    <div className={styles['month-filter-container']}>
      <label className={styles['month-select-label']} for="month-select">Month</label>

      <select className={styles['month-select-options']} name="months" id="month-select">
        <option value="">--Please choose an option--</option>
        <option value="dog">Dog</option>
        <option value="cat">Cat</option>
        <option value="hamster">Hamster</option>
        <option value="parrot">Parrot</option>
        <option value="spider">Spider</option>
        <option value="goldfish">Goldfish</option>
      </select>
    </div>
  )
}

export default MonthFilter;
