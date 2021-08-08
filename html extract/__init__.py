def table_extract(html_remove_blank: str):
    tr_start_index = 4
    tr_stop_index = -5
    tr_start_str = "<tr>"
    tr_stop_str = "</tr>"
    th_start_index = 4
    th_stop_index = -5
    th_start_str = "<th>"
    th_stop_str = "</th>"

    # remove table markup
    table_start_str = "<table>"
    table_stop_str = "</table>"
    table_start_index = len(table_start_str)
    table_stop_index = -len(table_stop_str)
    if html_remove_blank[:table_start_index] == table_start_str and html_remove_blank[
                                                                    table_stop_index:] == table_stop_str:
        html_remove_table = html_remove_blank[table_start_index:table_stop_index]
        # print(html_remove_table)
        table_split = "</table><table>"
        table_list = html_remove_table.split(table_split)
        # print(table_list)

        for i in table_list:
            # remove thead markup
            thead_start_str = "<thead>"
            thead_stop_str = "</thead>"
            thead_start_index = len(thead_start_str)
            thead_stop_index = -len(thead_stop_str)
            if i[:thead_start_index] == thead_start_str and thead_stop_str in i[thead_start_index:]:
                thead = i[thead_start_index:].split(thead_stop_str)[0]
                # print(thead)

                # remove tr markup
                thead_remove_tr = thead
                if thead[:tr_start_index] == tr_start_str and thead[tr_stop_index:] == tr_stop_str:
                    thead_remove_tr = thead[tr_start_index:tr_stop_index]
                    # print(thead_remove_tr)

                # remove th markup
                thead_remove_tr_th = thead_remove_tr
                if thead_remove_tr[:th_start_index] == th_start_str and thead_remove_tr[th_stop_index:] == th_stop_str:
                    thead_remove_tr_th = thead_remove_tr[th_start_index:th_stop_index]
                    # print(thead_remove_tr_th)
                # print(thead_remove_tr_th)
                thead_list = thead_remove_tr_th.split("</th><th>")
                print(thead_list)

            # remove tbody markup
            tbody_start_index = 7
            tbody_stop_index = -8
            tbody_start_str = "<tbody>"
            tbody_stop_str = "</tbody>"
            if i[:tbody_start_index] == tbody_start_str and tbody_stop_str in i[
                                                                              tbody_start_index:]:
                tbody = i[tbody_start_index:].split(tbody_stop_str)[0]
                # print(tbody)

                # remove tr markup
                tbody_remove_tr = tbody
                if tbody[:tr_start_index] == tr_start_str and tbody[tr_stop_index:] == tr_stop_str:
                    tbody_remove_tr = tbody[tr_start_index:tr_stop_index]
                    # print(tbody_remove_tr)

                # remove th markup
                tbody_remove_tr_th = tbody_remove_tr
                if tbody_remove_tr[:th_start_index] == th_start_str and tbody_remove_tr[th_stop_index:] == th_stop_str:
                    tbody_remove_tr_th = tbody_remove_tr[th_start_index:th_stop_index]
                    # print(tbody_remove_tr_th)
                print(tbody_remove_tr_th)
                tbody_list = tbody_remove_tr_th.split("</th><th>")
                print(tbody_list)
    else:
        print("Incorrect table format")


if __name__ == "__main__":
    html = """
    <table>
    <thead>
    <tr>
    <th>auto</th>
    <th>enum</th>
    <th>unsigned</th>
    <th>break</th>
    <th>extern</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>return</td>
    <td>void</td>
    <td>case</td>
    <td>float</td>
    <td>short</td>
    </tr>
    <tr>
    <td>volatile</td>
    <td>char</td>
    <td>for</td>
    <td>signed</td>
    <td>while</td>
    </tr>
    <tr>
    <td>const</td>
    <td>goto</td>
    <td>sizeof</td>
    <td>continue</td>
    <td>if</td>
    </tr>
    <tr>
    <td>static</td>
    <td>default</td>
    <td>struct</td>
    <td>do</td>
    <td>int</td>
    </tr>
    <tr>
    <td>switch</td>
    <td>double</td>
    <td>long</td>
    <td>typedef</td>
    <td>else</td>
    </tr>
    <tr>
    <td>register</td>
    <td>union</td>
    <td></td>
    <td></td>
    <td></td>
    </tr>
    <tr>
    <td><em>restrict</em></td>
    <td><em>inline</em></td>
    <td><em>_Bool</em></td>
    <td><em>_Complex</em></td>
    <td><em>_Imaginary</em></td>
    </tr>
    </tbody>
    </table>
    """
    html_remove_blank = html.replace("\n", "").replace("\r", "").replace(" ", "").replace("   ", "")
    table_extract(html_remove_blank)
