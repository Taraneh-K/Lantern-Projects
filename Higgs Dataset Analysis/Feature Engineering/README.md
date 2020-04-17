# Features Package:

This package is developed to help Data Scientists to accelerate Feature Engineering step of their projects. 
This package consists of 2 modules (FeatureEng and FeatureSelect).

## FeatureEng module:
Creates new feature columns for dataset based on selected aggregations and transformations. Following are the input parameters for this module:

        filepath : str
            the location of dataset. The string could be a URL. 
            Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is expected.
        
        header_type : int, list of int
            Row number(s) to use as the column names, and the start of the data.
            if header_type = 'infer', column names are inferred from the first line of the file, 
            if column names are passed explicitly then the behavior is identical to header=None. 
        
        categorical_col_name :  str, default = None
            The name of categorical columns
        
        label_col_name : str, default = None
            The name of label(target) column of dataframe

        list_agg_primitives : list[str or AggregationPrimitive], default = None
            list of Aggregation Feature types to apply.
                example types of aggreation for ft.dfs:
                ["sum", "std", "max", "skew", "min", "mean", "count",
				"percent_true", "num_unique", "mode"]

        list_trans_primitives : list[str or TransformPrimitive], default = ['multiply_numeric']
            List of Transform Feature functions to apply.
            example types of aggreation for ft.dfs:
            ["day", "year", "month", "weekday", "haversine", "num_words", "num_characters"]
        For more available perimitives : https://primitives.featurelabs.com/

        max_depth_value : int, default = 1
            Maximum allowed depth of features.

        threshold : int, default = 0.8
            Number between 0 and 1 which determines maximum features correlation limit
 
 
