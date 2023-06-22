import styles from '../../styles/Dashboard/IndicatorFilter.module.css';

function IndicatorFilter() {
  return (
    <div className={styles['indicator-filter-container']}>
      <label className={styles['indicator-select-label']} htmlFor="indicator-select">Indicators</label>
      <select className={styles['indicator-select-box']} name="indicators" id="indicator-select" multiple required>
        <option className={styles['indicator-select-options']} value="dog">Dog</option>
        <option className={styles['indicator-select-options']} value="cat">Cat</option>
        <option className={styles['indicator-select-options']} value="hamster">Hamster</option>
        <option className={styles['indicator-select-options']} value="parrot">Parrot</option>
        <option className={styles['indicator-select-options']} value="spider">Spider</option>
        <option className={styles['indicator-select-options']} value="goldfish">Goldfish</option>
      </select>
    </div>
  )
}

export default IndicatorFilter;
